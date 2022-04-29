caption_idx = list()
caption_file = open("data/XMCGAN_COCO_captions.txt", "r")
caption_text_list = caption_file.read()
caption_file.close()

captions = ['A baseball batter prepares to hit the ball while the catcher squats.', 'Three players stand and wait on the baseball field.', 'a baseball player with a bat gets ready to see a pitch ', 'A baseball player getting ready to swing a bat.', 'a baseball field that has baseball players in it']

for c in captions:
  print(type(c))
  if c in caption_text_list:
    idx = caption_text_list.index(c)
    caption_idx.append(idx)

print(caption_idx)