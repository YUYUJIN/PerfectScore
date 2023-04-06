# PerfectScore
> 반주를 재생하고 사용자가 반주에 맞추어 노래를 부르면 원곡(vocal)과 비교하여 유사도를 점수로 제공하는 프로그램입니다.
> 
> 배경음악 재생, 오디오 기록, 점수 계산 동작을 세 개의 쓰레드로 구성되어 있습니다.

<img src=https://img.shields.io/badge/python-3.8.0-green></img>
<img src=https://img.shields.io/badge/numpy-1.23.5-yellow></img>
<img src=https://img.shields.io/badge/librosa-0.9.2-orange></img>
<img src=https://img.shields.io/badge/pyaudio-0.2.12-yellowgreen></img>
<img src=https://img.shields.io/badge/scikit--learn-1.2.0-lightgrey></img>

## How to use
```
git clone https://github.com/YUYUJIN/PerfectScore.git
cd PerfectScore
pip install -r requirements.txt
python app.py
```

## Information
> 반주와 원곡자의 보컬을 준비하기 위해서 다양한 방식으로 준비할 수 있습니다. 이 프로젝트에서는 spleeter를 사용하여 반주와 보컬을 준비하였습니다.
>
> github link : https://github.com/deezer/spleeter
```
pip install spleeter
cd [음원 파일 경로]
spleeter separate -p spleeter:2stems -o output [음원 파일]
```
> 예시 음원 파일의 반주를 libsora를 이용하여 음계 단위로 성분 분석을 하면 다음과 같습니다.
<img src=https://github.com/YUYUJIN/PerfectScore/blob/main/features/accompaniment.png></img>
> 마찬가지로 분리한 보컬을 분석해보면 다음과 같습니다.
<img src=https://github.com/YUYUJIN/PerfectScore/blob/main/features/vocal.png></img>
> 보컬 부분만 사용하여 정답지를 단위 시간 당 음계의 강도를 사용하는 벡터를 준비합니다.
>
> 반주에 맞추어 사용자에게 음성을 입력 받고 마찬가지로 libsora를 이용하여 음성을 음계로 벡터화를 진행한 뒤에 코사인 유사도로 단위 시간 당 유사도를 비교합니다.
<img src=https://wikimedia.org/api/rest_v1/media/math/render/svg/2a8c50526e2cc7aa837477be87eff1ea703f9dec></img>
> 전체 시간 중에 유사도가 기준치를 넘는 구간의 비율로 점수를 계산합니다.
