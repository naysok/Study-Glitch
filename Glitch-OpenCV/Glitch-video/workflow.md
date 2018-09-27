# workflow.md



**mp4 (1280 × 720), src_mov**  

↓ (ffmpeg) // ok  

**Slicing-jpg (1280 × 720), src_slicing**  

↓ (python, ~~PIL~~ Pillow) // ok  

**Cropped-jpg(720x720), src_cropped**  

↓ (python, opencv) // ok??  

**Glitch-jpg (720x720), src-glitch**  

↓ (ffmpeg) // ok  

**mp4**



---  


### ffmpeg memo  

SlicingImage-from-Video  

```bash
ffmpeg -i 180917.mp4 -ss 0 -r 30 -q 1 image-%5d.jpg

```



Video-from-Images

```bash
ffmpeg -framerate 30 -start_number 0 -i image-%05d.jpg -r 30 -an -vcodec libx264 -pix_fmt yuv420p out1.mp4
```


---  

### Effects  

- Blur  
![photo](Effects/Blur.jpg)  

- Draw Horizontal Line  
![photo](Effects/Draw-horizontal-line.jpg)  

- Draw Vertical Line  
![photo](Effects/Draw-vertical-line.jpg)  

- Edit Blue Channel  
![photo](Effects/Edit-Blue-Channel.jpg)  

- Edit Red Channel  
![photo](Effects/Edit-Red-Channel.jpg)  

- Edit Green Channel  
![photo](Effects/Edit-Green-Channel.jpg)  

- Scratch Horizontal  
![photo](Effects/Scratch-horizontal.jpg)  

- Scratch Vertical  
![photo](Effects/Scratch-vertical.jpg)





