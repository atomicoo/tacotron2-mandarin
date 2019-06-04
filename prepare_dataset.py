"""Datasets preprocessor for TWL ASR Speech."""
__author__ = 'Joee'

import os
import sys
import time
import argparse
import unicodedata
import librosa

from tqdm import tqdm
from hparams import hparams


def run_prepare(args, hparams):
    if args.dataset == 'BIAOBEI':
        dataset_name = 'biaobei_48000'
        dataset_path = os.path.join(os.getcwd(), args.dataset)

        if os.path.isdir(dataset_path):
            print("BIAOBEI dataset folder already exists")
            sys.exit(0)

        os.mkdir(dataset_path)
        dataset_path = os.path.join(dataset_path, dataset_name)
        os.mkdir(dataset_path)

        sample_rate = 48000  # original sample rate
        total_duration = 0

        raw_dataset_path = os.path.join(os.getcwd(), 'BZNSYP')

        text_file_path = os.path.join(raw_dataset_path, 'ProsodyLabeling', '000001-010000.txt')
        try:
            text_file = open(text_file_path, 'r', encoding='utf8')
        except FileNotFoundError:
            print('text file no exist')
            sys.exit(0)

        def normalize_text(text):
            """normalize text format"""
            text = ''.join(char for char in unicodedata.normalize('NFD', text)
                           if unicodedata.category(char) != 'Mn')
            return text.strip()

        def normalize_wave(wave):
            """normalize wave format"""
            wave = librosa.resample(wave, sample_rate, hparams.sample_rate)
            return wave

        for index, each in tqdm(enumerate(text_file.readlines())):
            if index % 2 == 0:
                basename = each.strip().split()[0]
            else:
                text = normalize_text(each)
                text_file = os.path.join(dataset_path, '{}.trn'.format(basename))
                with open(text_file, 'w', encoding='utf8') as f:
                    f.write(text)
                wave_file_path = os.path.join(raw_dataset_path, 'Wave', '{}.wav'.format(basename))
                if not os.path.exists(wave_file_path):
                    # print('wave file no exist')
                    continue
                try:
                    wave, sr = librosa.load(wave_file_path, sr=None)
                except EOFError:
                    # print('wave format error')
                    continue
                if not sr == sample_rate:
                    # print('sample rate no match')
                    continue
                # wave = normalize_wave(wave)
                duration = librosa.get_duration(wave)
                total_duration += duration
                wave_file = os.path.join(dataset_path, '{}.wav'.format(basename))
                librosa.output.write_wav(wave_file, wave, hparams.sample_rate)

        text_file.close()
        print("total audio duration: %ss" % (time.strftime('%H:%M:%S', time.gmtime(total_duration))))
    elif args.dataset == 'THCHS-30':
        dataset_name = 'thchs30_16000'
        dataset_path = os.path.join(os.getcwd(), args.dataset)

        if os.path.isdir(dataset_path):
            print("{} dataset folder already exists".format(args.dataset))
            sys.exit(0)
        
        os.mkdir(dataset_path)
        dataset_path = os.path.join(dataset_path, dataset_name)
        os.mkdir(dataset_path)

        sample_rate = 16000  # original sample rate
        total_duration = 0

        def normalize_text(text):
            """normalize text format"""
            text = ''.join(char for char in unicodedata.normalize('NFD', text)
                           if unicodedata.category(char) != 'Mn')
            return text.strip()

        def normalize_wave(wave):
            """normalize wave format"""
            wave = librosa.resample(wave, sample_rate, hparams.sample_rate)
            return wave

        raw_dataset_path = os.path.join(os.getcwd(), 'data_thchs30', 'data')

        for root, dirs, files in os.walk(raw_dataset_path):
            for file in tqdm(files):
                if not file.endswith('.wav.trn'):
                    continue
                parts = os.path.join(root, file).split('\\')
                basename = parts[-1][:-8]
                text_file = os.path.join(raw_dataset_path, '{}.wav.trn'.format(basename))
                if not os.path.exists(text_file):
                    # print('text file {}.wav.trn no exist'.format(basename))
                    continue
                with open(text_file, 'r', encoding='utf8') as f:
                    lines = f.readlines()
                text = lines[1].rstrip('\n')
                text = normalize_text(text)
                text_file = os.path.join(dataset_path, '{}.trn'.format(basename))
                with open(text_file, 'w', encoding='utf8') as f:
                    f.write(text)
                wave_file = os.path.join(raw_dataset_path, '{}.wav'.format(basename))
                if not os.path.exists(wave_file):
                    # print('wave file {}.wav no exist'.format(basename))
                    continue
                try:
                    wave, sr = librosa.load(wave_file, sr=None)
                except EOFError:
                    # print('wave file {}.wav format error'.format(basename))
                    continue
                if not sr == sample_rate:
                    # print('sample rate of wave file {}.wav no match'.format(basename))
                    continue
                duration = librosa.get_duration(wave)
                total_duration += duration
                # wave = normalize_wave(wave)
                wave_file = os.path.join(dataset_path, '{}.wav'.format(basename))
                librosa.output.write_wav(wave_file, wave, hparams.sample_rate)

        print("total audio duration: %ss" % (time.strftime('%H:%M:%S', time.gmtime(total_duration))))
    elif args.dataset == 'AISHELL-2':
        dataset_name = 'aishell2_16000'
        dataset_path = os.path.join(os.getcwd(), args.dataset)

        if os.path.isdir(dataset_path):
            print("{} dataset folder already exists".format(args.dataset))
            sys.exit(0)

        os.mkdir(dataset_path)
        dataset_path = os.path.join(dataset_path, dataset_name)
        os.mkdir(dataset_path)

        sample_rate = 16000  # original sample rate
        total_duration = 0

        raw_dataset_path = os.path.join(os.getcwd(), 'aishell2', 'dataAishell2')
        wave_dir_path = os.path.join(raw_dataset_path, 'wav')
        text_file_path = os.path.join(raw_dataset_path, 'transcript', 'aishell2_transcript.txt')
        try:
            text_file = open(text_file_path, 'r', encoding='utf8')
        except FileNotFoundError:
            print('text file no exist')
            sys.exit(0)

        def normalize_text(text):
            """normalize text format"""
            text = ''.join(char for char in unicodedata.normalize('NFD', text)
                           if unicodedata.category(char) != 'Mn')
            return text.strip()

        def normalize_wave(wave):
            """normalize wave format"""
            wave = librosa.resample(wave, sample_rate, hparams.sample_rate)
            return wave

        # for index, each in tqdm(enumerate(text_file.readlines())):
        #


def main():
    print('preparing dataset..')
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset", choices=['AISHELL-2', 'THCHS-30', 'BIAOBEI'], default='BIAOBEI', help='dataset name')
    args = parser.parse_args()
    
    run_prepare(args, hparams)


if __name__ == '__main__':
    main()
