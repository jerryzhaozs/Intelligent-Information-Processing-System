#加载模型
from keras.models import Model
from keras_transformer import get_model, decode
import pickle
path = 'C:\\Users\\Administrator\\Desktop\\sys\\server\\trans\\trans2\\middle_data\\'
with open(path + 'encode_input.pkl', 'rb') as f:
    encode_input = pickle.load(f)
with open(path + 'decode_input.pkl', 'rb') as f:
    decode_input = pickle.load(f)
with open(path + 'decode_output.pkl', 'rb') as f:
    decode_output = pickle.load(f)
with open(path + 'source_token_dict.pkl', 'rb') as f:
    source_token_dict = pickle.load(f)
with open(path + 'target_token_dict.pkl', 'rb') as f:
    target_token_dict = pickle.load(f)
with open(path + 'source_tokens.pkl', 'rb') as f:
    source_tokens = pickle.load(f)
print('Done')
model = get_model(
    token_num=max(len(source_token_dict), len(target_token_dict)),
    embed_dim=64,
    encoder_num=2,
    decoder_num=2,
    head_num=4,
    hidden_dim=256,
    dropout_rate=0.05,
    use_same_embed=False,
)
model.compile('adam', 'sparse_categorical_crossentropy')
model_path='C:\\Users\\Administrator\\Desktop\\sys\\server\\trans\\trans2\\model\\final.h5'
model.load_weights(model_path)
target_token_dict_inv = {v: k for k, v in target_token_dict.items()}
print('Done')

from keras.preprocessing import sequence
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import jieba
import requests

def get_input(seq):
    seq = ' '.join(jieba.lcut(seq, cut_all=False))
    # seq = ' '.join(seq)
    seq = seq.split(' ')
    print(seq)
    # ------------------
    new_seq=[]
    for x in seq:
        if x in source_token_dict:
            new_seq.append(x)
            continue
        now=x
        while True:
            if now[0] in source_token_dict:
                new_seq.append(now[0])
            if now[1:] in source_token_dict:
                new_seq.append(now[1:])
                break
            else:
                now=now[1:]
                # -----------------------
    new_seq = ['<START>'] + new_seq + ['<END>']
    new_seq = new_seq + ['<PAD>'] * (34 - len(new_seq))
    print(new_seq)
    newest_seq = [source_token_dict[x] for x in new_seq]
            
    flag=True
    return flag, newest_seq
def get_ans(seq):
    decoded = decode(
    model,
    [seq],
    start_token=target_token_dict['<START>'],
    end_token=target_token_dict['<END>'],
    pad_token=target_token_dict['<PAD>'],
    )
    return(' '.join(map(lambda x: target_token_dict_inv[x], decoded[0][1:-1])))

seqs=['你好']
for seq in seqs:
    if seq == 'x':
        break
    flag, seq = get_input(seq)
    get_ans(seq)