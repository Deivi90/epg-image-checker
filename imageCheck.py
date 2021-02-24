import json
import sys
import os
import requests # to get image from the web
import shutil # to save it locally
import csv

#JSON_IMAGES_NAMES
jsonImages = ['image_large',
            'cover',
            'portrait',
            'image_clean_horizontal',
            'image_base_vertical',
            'image_clean_square',
            'background',
            'image_base_square',
            'image_clean_vertical',
            'image_medium',
            'image_base_horizontal',
            'image_background',
            'image_still',
            'image_small',
            'image_sprites',
            'imageEpg']
   
#JSON_EPG_FILES 
JSON_EPG_FILES = ['Precheck_uat_CABA_GENERIC.json',
            'Precheck_uat_CA_GENERIC.json',
            'Precheck_uat_CB_GENERIC.json',
            'Precheck_uat_CH_GENERIC.json',
            'Precheck_uat_FO_GENERIC.json',
            'Precheck_uat_GENERIC.json',
            'Precheck_uat_JY_GENERIC.json',
            'Precheck_uat_MI_GENERIC.json',
            'Precheck_uat_MZ_GENERIC.json',
            'Precheck_uat_NQ_GENERIC.json',
            'Precheck_uat_PBA_GENERIC.json',
            'Precheck_uat_PBA_PBA380.json',
            'Precheck_uat_SA_GENERIC.json',
            'Precheck_uat_SF_GENERIC.json',
            'Precheck_uat_SF_SF3855.json',
            'Precheck_uat_TU_GENERIC.json']

lineWidth = 30


def main():
  args = sys.argv[1:]
  if len(args) != 1:
    print("Usar: {} 'Path archivo json'".format(sys.argv[0]))
    sys.exit(1)     
  jsonFile = open(args[0],)
  
  epgJson = json.load(jsonFile)
  line = '.'*lineWidth
  urlError = {}
  # i = 0
  for channel in epgJson: 
      # i= 1 + i
      title = channel['title']
      print(title)
      print("----------------")
      for image in jsonImages:
          imageUrl = channel[image]
          response = requests.get(imageUrl)
          if(response.status_code == 200):
            print(image + line[len(image):]+ 'Ok  ' + imageUrl)  
          else:
            print(image + line[len(image):] + "Error " + str(response.status_code))
            urlError[title] = {image : "Error " + str(response.status_code)}
          response.close()  
      print()
      # if i==4:
        # break

  with open('output.csv', 'w',newline='') as output:
    writer = csv.writer(output)
    for title in urlError.keys():
        for key in urlError[title]:
            writer.writerow([title,key,urlError[title][key]])

 
if __name__ == "__main__":
  main()
