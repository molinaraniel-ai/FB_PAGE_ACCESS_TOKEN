import os
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

print("Generando video de Messi...")
background = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=75)
txt_clip = TextClip("¡Messi, Leyenda del Fútbol! - Grupo 1", fontsize=50, color='white', size=(1000, 1920))
txt_clip = txt_clip.set_duration(75).set_position('center')

video = CompositeVideoClip([background, txt_clip])
video.write_videofile("resultado_messi.mp4", fps=24, codec='libx264', audio_codec='aac')
print("¡Video resultado_messi.mp4 generado con éxito!")
