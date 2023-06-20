import playaudio

answer = input('Play audio? y/n: ')

while answer == 'y':
    print('Please wait for the audio to finish!')
    playaudio.playaudio('assets/w.mp3')
    answer = input('Play audio? y/n: ')
