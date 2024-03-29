# Anime Face Dataset
The dataset can be found [here](https://drive.google.com/file/d/1HG7YnakUkjaxtNMclbl2t5sJwGLcHYsI/view?usp=sharing). Also checkout [this repository](https://github.com/bchao1/Anime-Generation) for anime generation using generative adversarial networks.

### 2022/6/26 update
Due to copyright issues, I have made the dataset private. You can still use the scripts in this repo to scrape the dataset yourself, but use at you own discretion. I am also working on new version of this dataset, but I will only publish scraping and post-processing scripts since I cannot distribute the images. Stay tuned!

## Samples 
<p align="center">
    <img src="./test.jpg" width="600">
</p>

## Disclaimer
This dataset should only be used for educational purposes. Please cite the source if you use this dataset in your projects, research papers, and etc. Consider starring this repo if you find it useful!
   
One user has uploaded this dataset to [Kaggle](https://www.kaggle.com/datasets/splcher/animefacedataset). If you're downloading the dataset from the Kaggle source, I would appreciate if you also cite this repository.   

## Author 
Brian Chao

## Dataset Description
This is an dataset consisting of 63632 high-quality anime faces scraped from www.getchu.com, which are then cropped using the anime face detection algorithm in https://github.com/nagadomi/lbpcascade_animeface. Images sizes vary from 90 * 90 ~ 120 * 120 (you can simply rescale them before using them).
   
Compared to other widely used datasets (such as the *danbooru* dataset, which is actually quite a mess), this dataset contains high quality anime character images with clean background and rich colors.
   
However, few outliers are still present in the dataset:
- Bad cropping results
- Some non-human faces.


Feel free to contribute to this dataset by adding images of similar quality or adding image labels. 

## Source Code
I made the web-scraping and face-detection code open-source. Make modifications as you wish. To scrape the pictures directly from the website and detect the faces on your own, type the following commands:
```
git clone https://github.com/bchao1/Anime-Face-Dataset.git
cd Anime-Face-Dataset/src
python3 scrape.py
python3 detect.py
```
The scraped images will be in the `./src/images` folder, while the cropped images (character faces) will be in the `./src/cropped` folder.

## Citing Anime Face Dataset

If you find this dataset helpful, I would appreciate if you cite it:

```
@online{chao2019/online,
  author       = {Brian Chao},
  title        = {Anime Face Dataset: a collection of high-quality anime faces.},
  date         = {2019-09-16},
  year         = {2019},
  url          = {https://github.com/bchao1/Anime-Face-Dataset}
}
```

