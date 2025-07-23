
npl에 대해 공부한 내용을 정리함.

각 폴더의 내용을 설명한다. 


## 1. basics
기본적인 encoder-decoder를 LSTM으로 구현함.

## 2. transformers

**transformer**([Attentions Is All You Need](https://arxiv.org/pdf/1706.03762))를 이해하기 위해 [`딥 러닝을 이용한 자연어 처리 입문`](https://wikidocs.net/book/2155)의 <br> [16-01 트랜스포머(Transformer)](https://wikidocs.net/31379)을 참고하였고, [The Annotated Transformer-old](https://nlp.seas.harvard.edu/2018/04/03/attention.html), <br> [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)의 코드를
라인 단위로 분석하고 실행해본 과정을 정리함.

### 각 파일 설명

#### 2.1 **Annotated Transformer**
 [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/)의 코드를 분석하고 실행함.

----------------------
| 파일명 | descrption |
|-------|-------------|
|[transformer_v2.py](./transformers/transformer_v2.py) | transformer 모델과 토큰 처리를 위한 모든 코드가 포함되어 있고, Multi-GPU(4)로 훈련가능함 de-en |
|[trainning_the_annotated_transformer_decoding.ipynb](./transformers/trainning_the_annotated_transformer_decoding.ipynb)| 싱글 gpu로 transformer를 훈련 시킬수 있음. de-en 훈련 시킴|
|[Results for Transformer.ipynb](./transformers/Results%20for%20Transformer.ipynb) | 훈련시킨 모델을 불러와 테스트 할 수 있음. |

#### 2.2 **Annotated Transformer-old**

----------------------
| 파일명 | descrption |
|-------|-------------|
|[Batch_datagen.ipynb](./transformers/Batch_datagen.ipynb)| Batch 클래스를 분석하고 사용법을 정리함, example로 훈련 시키기 위한 batch 데이터를 만듬|
|[decoder_2nd_layer.ipynb](./transformers/decoder_2nd_layer.ipynb)|디코더의 두번째 서브층인 인코더-디코더 어텐션을 분석함|
|[decoder_ex.py](./transformers/decoder_ex.py) | encoder과 decoder를 manual로 만들어 봄|
|[decoder_selfattention_look_a_head_mask.ipynb](./transformers/decoder_selfattention_look_a_head_mask.ipynb)| 디코더의 첫번째 서브층의  셀프 어텐션과 룩-어헤드 마스크를 분석|
|[encoder.ipynb](./transformers/encoder.ipynb) | 인코더만 분석함. 패딩, skip, layer normalization을 분석함. layer normalization는 논문 구현과 다름|
|[full_model.ipynb](./transformers/full_model.ipynb) | full model를 만드는 과정을 테스트와 입력 데이터를 만드는 과정 정리|
|[greedy_decoding.ipynb](./transformers/greedy_decoding.ipynb) | greed_decoding 자료 -chat-gpt|
|[havard_mulitihead_attention.ipynb](./transformers/havard_multihead_attention.ipynb) | mulitihead_attention 코드 설명|
|[MultiheadAttention.ipynb](./transformers/MultiHeadAttention.ipynb)| 다른 버전 설명|
|[Understanding_Masking_in_PyTorch_for_Attention_Mechanisms.ipynb](./transformers/Understanding_Masking_in_PyTorch_for_Attention_Mechanisms.ipynb)| 마스킹 방법들을 설명함|
|[Label Smoothing.ipynb](./transformers/Label%20Smoothing.ipynb)| Regularization 설명 |
|[Position-wise FFNN.ipynb](./transformers/Position-wise%20FFNN.ipynb)| 코드 설명 |
|[positional_encodingII.ipynb](./transformers/positional_encodingII.ipynb)| positional_encoding 설명|
|[transformers.py](./transformers/transformers.py)|Annotated Transformer-old 코드를 모아놓음|
|[understanding_trainning.ipynb](./transformers/understanding_trainning.ipynb)| 다른 pytorch 훈련법과 비교해 봄 |
|[trainning.ipnb](./transformers/training.ipynb)| 랜덤 데이터로 훈련시키고, greedy_decoding함.|

--- 
#### 2.2.1 실행환경 (docker): 
docker에서 실행될 수 있음.  
[Dockerfile](./Dockers/The_Annotated_transformation/Dockerfile) 파일과 [build.sh](./Dockers/The_Annotated_transformation/build.sh), [run.sh](./Dockers/The_Annotated_transformation/run.sh) 참고 해라.

---

#### 2.3 **custom dataset 훈련시키는 예제 (영어-한국어)**  
Annotated Transformer-old로 초 심플한 영-한 번역기를 훈련 시킴.

----------------------
| 파일명 | descrption |
|-------|-------------|
|[custom_dataset_ex1.ipynb](./transformers/custom_dataset_ex1.ipynb)| nltk로 한국어, 영어를 토큰화 함|
|[custom_dataset_ex2.ipynb](./transformers/custom_dataset_ex2.ipynb)| 한국어는 Okt로   영어는 spacy로 토큰화|
|[make a custom vocab.ipynb](./transformers/make%20a%20custom%20vocab%20.ipynb) | 한국어를 토큰화, id 변환, 패딩등 특수문자를 붙이는 연습을 해 봄 |
|[simple_custom_trainning.ipynb](./transformers/simple_custom_training.ipynb)| 간단한 영-한 번역기를 훈련시킴, GPU에서 동작하고 Dataloader를 사용하도록 코드를 수정함. 32 example의 코퍼스 임.|
---



















