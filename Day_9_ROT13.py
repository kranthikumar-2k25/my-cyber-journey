import codecs

message = "gurl nernq gur cnffjbeq" 

secret = codecs.decode(message, 'rot_13')

print("Decoded Message:", secret)
