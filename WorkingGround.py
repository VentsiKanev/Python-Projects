import winsound

#insound.Beep(432, 500)


sound_button = input("Would you like to hear win sound? Yes/no:").lower().strip()

if sound_button == "yes":
    winsound.Beep(432, 500)
elif sound_button == "no":
     exit()

