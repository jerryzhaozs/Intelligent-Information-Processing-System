<template>
    <div class="q-pa-md row justify-center">
        <div style="width: 100%; max-width: 800px">
            <q-scroll-area ref="scrollArea" style="height: 1000%;" :visible="false" :thumb-style="thumbStyle">
                <div class="q-pa-lg col justify-center">
                    <q-chat-message v-for="(item, index) in messages" :key="index" 
                    :sent="item.type!='received'"
                    :bg-color="getBgColor(item.type,1)"
                    :name="getBgColor(item.type,2)"
                    >
                    {{ item.text }}
                    <div v-if="item.imgUrl!=''">
                        <img
                        alt="uploaded pic"
                        :src="item.imgUrl"
                        style="width: 100%; max-width: 800px;height:350px"
                        >
                    </div>
                    </q-chat-message>
                    <q-chat-message v-if="isReply<1" bg-color="green-1">
                        <q-spinner-dots size="2rem" />
                    </q-chat-message>
                </div>
            </q-scroll-area>
            <q-input outlined bottom-slots v-model="content" label="来说点什么吧 （Enter = 发送）" @keyup.enter="sendMessage">
                <template v-slot:append>
                <q-btn round dense flat icon="send" @click="sendMessage"/>
                </template>
            </q-input>
            <!-- <div>
                <q-input outlined bottom-slots v-model="content" label="来说点什么吧 （Enter = 发送）" counter @keyup.enter="sendMessage">
                <template v-slot:append>
                <q-btn round dense flat icon="send" @click="sendMessage"/>
                </template>
                </q-input>
                <q-input outlined v-model="content" label="来说点什么吧 （Enter = 发送）" @keyup.enter="sendMessage"/>
                <q-btn color="primary" label="发送" @click="sendMessage"/> 
            -->
            <input type="file" id="myFileInput" ref="fileInput" style="display:none"  @change="handleFileUpload">
        </div>
    </div>
</template>
  
<script>
  export default {
  name: "Chatbot",
  components: {
  },
  data() {
    return {
        thumbStyle: {
        right: '2px',
        borderRadius: '5px',
        // backgroundColor: '#2ba245',
        backgroundColor: '#ffffff',
        width: '5px',
        opacity: 0.75
      },
        position:10000,
        isReply:1,
        content:'',
        files:'',
      messages: [
        { text: "你好！", type: "received", imgUrl:""},
        { text: "请先上传图片", type: "received", imgUrl:""},
      ],
    };
  },
  methods:{
    animateScroll(){
        this.$refs.scrollArea.setScrollPosition('vertical', this.position, 300)
    },
    getBgColor(atype,tt){
        if(tt==1){
            if(atype=='received'){
                return 'green-1'
            }else{
                return 'positive'
            }
        }else if(tt==2){
            if(atype=='received'){
                return 'Bot'
            }else{
                return '我'
            }
        }
    },
    handleFileSelect(){
        this.$refs.fileInput.click();
    },
    handleFileUpload(event){
        var file = event.target.files[0];
        var formData = new FormData();
        document.getElementById('myFileInput').value = '';
        formData.append('file', file);
        // 发送 formData 到服务器
        this.$axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
        })
        .then(response => {
          this.messages.push({text:'图片上传成功',type:'received', imgUrl:"http://localhost:5000/static/pic/"+response.data+".png"})
          this.files=''
        //   this.animateScroll()
        //   console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          this.files=''
        });
    },
    cleanHistory(){
        this.messages=[
        { text: "你好！", type: "received", imgUrl:""},
        { text: "请先上传图片", type: "received", imgUrl:""},
      ]
    },
    showPic(id){
        this.messages.push({text:"处理后的图像为",type:'received', imgUrl:"http://localhost:5000/static/pic/"+id+".png"})

    },
    sendMessage(){
        if (this.content== "") return;
        this.messages.push({text:this.content,type:'sent', imgUrl:""});
        this.isReply-=1;
        var now_content=this.content
        this.content=''
        this.animateScroll()
        this.$axios.post("http://localhost:5000/" ,{
        "params":{
          "content":now_content,
        }
        }).then((res)=> {
            this.isReply+=1;
            if(res.data=='clear'){
                this.cleanHistory()
            }else if(res.data=='inputPic'){
                this.handleFileSelect()
                this.animateScroll()
            }else if(res.data[0]=='c'){
                this.showPic(res.data.substring(1))
                this.animateScroll()
            }else{
                // console.log('什么？')
                this.messages.push({text:res.data,type:'received', imgUrl:""})
                this.animateScroll()
            }
            
        })
    }
  },
};
  </script>