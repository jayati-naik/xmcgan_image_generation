import numpy as np
import os
from collections import defaultdict
from PIL import Image

import random

def create_image_files(source_dir: str='./', target_dir: str='./'):
  all_npy_files = os.listdir(source_dir)
  index = defaultdict(int)
  count = 0
  for filename in all_npy_files:
    if filename[-4:] == '.npy':
      batch_data = np.load(f'{source_dir}/{filename}')
      batch_data = batch_data.astype(np.uint8)
      for image, name in zip(batch_data, filename[:-4].split('-')[0].split('_')):
        count += 1
        prefix = f'COCO_val2014_{"0" * (12-len(name))}'
        img_filename = f"{target_dir}{prefix}{name}-{index[name]}.png"
        index[name]+=1
        im = Image.fromarray(image)
        im.save(img_filename)
        print(f"Saved {img_filename}")
  print(f"Total files save: {count}")


def create_noise_files(source_dir: str='./', target_dir: str='./'):
  all_npy_files = os.listdir(source_dir)
  index = defaultdict(int)
  z_list = list()
  for filename in all_npy_files:
    if filename[-4:] == '.npy':
      batch_data = np.load(f'{source_dir}/{filename}')
      for z, name in zip(batch_data, filename[:-4].split('-')[0].split('_')):
        index[name]+=1
        z_list.append(z)
  
  with open('/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/final/XMCGAN_COCO_noise.npy', 'w') as f:
    f.write("%s,\n"%(z_list))
  

if __name__ == '__main__':
  '''
  # Output Directories
  source_img_dir = '/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/images/normal/'
  target_img_dir = '/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/final/images/normal/'

  # Split images from batch for image to caption index
  create_image_files(source_img_dir, target_img_dir)

  source_noise_dir = '/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/images/normal/'
  target_noise_dir = '/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/final/images/normal/'

  # Split noise from batch for image to caption index
  create_noise_files(source_noise_dir, target_noise_dir)
  '''
  # Read batch_file.csv file
  with open('/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/XMCGAN_COCO_batch_file.csv') as f:
    image_caption_list = [line.strip() for line in f]
  
  with open('/ifs/loni/faculty/thompson/four_d/jnaik/xmcgan_image_generation/output/final/XMCGAN_COCO_filenames.csv', 'a') as f:
    output = list()
    for sample in image_caption_list:
      print(sample)
      filename, text_index = sample.split(',')

      filenames = filename.split('_')
      text_indexes = text_index.split('_')

      num_datapoints = len(filenames)

      for i in range(num_datapoints):
        f.write("(%s,%s,%s)\n"%(filenames[i], text_indexes[i], 5))


