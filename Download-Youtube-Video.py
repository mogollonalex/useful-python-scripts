# Debemos instalar las siguientes librerías
# pip install pytube

from pytube import YouTube 

def descargar_Video(yt):
  # Filtrar los objetos con extensión mp4
  my_streams = yt.streams.filter(file_extension='mp4', only_video=True)
  for streams in my_streams:
    # Imprime en la pantalla el itag, las resolución y la extensión
    print(f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}")
        
  # Ingresa el itag con la extensión y resolución de preferencia
  input_itag = input("Ingresa un valor de itag : ")
  # Obtienes el valor para descargar
  video = yt.streams.get_by_itag(input_itag)
  
  # Finalmente se descarga el vídeo
  video.download()
  print("Vídeo descargado como",yt.title+".mp4")
  
link = input("Ingresa la URL del vídeo de YouTube: ")
# Creando el objeto YouTube.
yt = YouTube(link) 

# LLamamos la función..
descargar_Video(yt)
