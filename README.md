# 此仓库不再维护，最新工作见 [ParallelTTS](https://github.com/atomicoo/ParallelTTS)。
# This repository is no longer maintained. Go [ParallelTTS](https://github.com/atomicoo/ParallelTTS) for the latest work.
# tacotron-2-mandarin-griffin-lim
Tensorflow implementation of DeepMind's Tacotron-2. A deep neural network architecture described in this paper: [Natural TTS synthesis by conditioning Wavenet on MEL spectogram predictions](https://arxiv.org/abs/1712.05884)

## Repo Structure ##
	tacotron-2-mandarin-griffin-lim
	|--- datasets
	|--- logs-Tacotron
	     |--- eval-dir
	     |--- plots
	     |--- taco_pretrained
	     |--- wavs
	|--- papers
	|--- prepare
	|--- tacotron
	     |--- models
	     |--- utils
	|--- tacotron_output
	     |--- eval
	     |--- logs-eval
	          |--- plots
	          |--- wavs
	|--- training_data
	     |--- audio
	     |--- linear
	     |--- mels

## Samples ##

There are some synthesis samples [here](<https://github.com/Joee1995/tacotron2-mandarin-griffin-lim/tree/master/samples>).  

## Pretrained ##

you can get pretrained model [here](<https://github.com/Joee1995/tacotron2-mandarin-griffin-lim/tree/master/pretrained>).

## Quick Start ##

> OS: Ubuntu 16.04

**Step (0)** - Git clone repository

```
git clone https://github.com/Joee1995/tacotron-2-mandarin-griffin-lim.git
cd tacotron-2-mandarin-griffin-lim/
```

**Step (1)** - Install dependencies

1. Install Python 3 (python-3.5.5 for me)

2. Install TensorFlow (tensorflow-1.10.0 for me)

3. Install other dependencies

   ```
   pip install -r requirements.txt
   ```

**Step (2)** - Prepare dataset

1. Download dataset [BIAOBEI](<https://www.data-baker.com/open_source.html>) or [THCHS-30](<http://www.openslr.org/18/>)

   After that, your doc tree should be: 

   ```
   tacotron-2-mandarin-griffin-lim
   |--- ...
   |--- BZNSYP
        |--- ProsodyLabeling
             |--- 000001-010000.txt
        |--- Wave
   |--- ...
   ```

2. Prepare dataset (default is `BIAOBEI`)

   ```
   python prepare_dataset.py
   ```

   If preparing `THCHS-30`, you can use parameter `--dataset=THCHS-30`. 

   After that, you can get a folder `BIAOBEI` as follow: 

   ```
   tacotron-2-mandarin-griffin-lim
   |--- ...
   |--- BIAOBEI
        |--- biaobei_48000
   |--- ...
   ```

3. Preprocess dataset (default is `BIAOBEI`)

   ```
   python preprocess.py
   ```

   If prrprocessing `THCHS-30`, you can use parameter `--dataset=THCHS-30`. 

   After that, you can get a folder `training_data` as follow: 

   ```
   tacotron-2-mandarin-griffin-lim
   |--- ...
   |--- training_data
        |--- audio
        |--- linear
        |--- mels
        |--- train.txt
   |--- ...
   ```

**Step (3)** - Train tacotron model

```
python train.py
```

More parameters, please see [train.py](<https://github.com/Joee1995/tacotron-2-mandarin-griffin-lim/blob/master/train.py>). 

After that, you can get a folder `logs-Tacotron` as follow: 

```
tacotron-2-mandarin-griffin-lim
|--- ...
|--- logs-Tacotron
     |--- eval-dir
     |--- plots
     |--- taco_pretrained
     |--- wavs
|--- ...
```

**Step (4)** - Synthesize audio

```
python synthesize.py
```

More parameters, please see [synthesize.py](<https://github.com/Joee1995/tacotron2-mandarin-griffin-lim/blob/master/synthesize.py>). 

After that, you can get a folder `tacotron_output` as follow: 

```
tacotron-2-mandarin-griffin-lim
|--- ...
|--- tacotron_output
     |--- eval
     |--- logs-eval
          |--- plots
          |--- wavs
|--- ...
```

## References & Resources ##
[Rayhane-mamah/Tacotron-2](<https://github.com/Rayhane-mamah/Tacotron-2>) 

