"""Computer Vision Lab 01: Color-space visualization. / 计算机视觉实验1"""
from pathlib import Path
import argparse, cv2
import matplotlib.pyplot as plt

def main():
    p=argparse.ArgumentParser(); p.add_argument("image"); p.add_argument("--outdir",default="outputs"); a=p.parse_args()
    out=Path(a.outdir); out.mkdir(parents=True,exist_ok=True)
    bgr=cv2.imread(a.image,cv2.IMREAD_COLOR)
    if bgr is None: raise FileNotFoundError(a.image)
    rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB); gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY); hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV); lab=cv2.cvtColor(rgb,cv2.COLOR_RGB2LAB)
    print("shape:",rgb.shape,"dtype:",rgb.dtype,"min/max:",(int(rgb.min()),int(rgb.max())))
    fig,ax=plt.subplots(1,4,figsize=(12,3)); data=[(rgb,None,"RGB"),(gray,"gray","Gray"),(hsv,None,"HSV (raw channels)"),(lab,None,"Lab (raw channels)")]
    for a0,(im,cmap,title) in zip(ax,data): a0.imshow(im,cmap=cmap); a0.set_title(title); a0.axis("off")
    fig.tight_layout(); fig.savefig(out/"color_space_overview.png",dpi=160); plt.show()
    # TODO: visualize individual channels; compare representative pixels/regions; reconstruct RGB.
if __name__=="__main__": main()
