import time
import os
import colorama
lyrics1= r"""
**enter lyrics** """ #triple quotes preserve line breaks

def parse_lyrics(lyrics):
    individuals=lyrics.strip().splitlines()
    timings=["" for _ in range(len(individuals))]
    indiv_lyrics=["" for _ in range(len(individuals))]
    
    
    for index1,i in enumerate(individuals): #could be a more efficient way but whatever no fuss
        #this loop splits up durations and lyrics
        if i[0]!='[':
            individuals.remove(i)
        isLyric=False
        for c in i:
            
            if c=='[':
                continue
            if c == "]":
                isLyric=True
                continue
            elif not isLyric:
                timings[index1]+=c
            if isLyric:
                indiv_lyrics[index1]+=c

    #print(individuals)
    print(timings)
    print(indiv_lyrics)

    timings_secs=[0 for _ in timings]
    for index,ts in enumerate(timings): # turn timings into secs
        isMins=True
        mins=''
        secs=''
        for c in ts:
            if c==':':
                isMins=False
                continue
            if isMins:
                mins+=c
            else:
                secs+=c
        timings_secs[index]+=float(mins)*60+float(secs)
    print(timings_secs)
    durations=[round(timings_secs[i+1]-timings_secs[i],2) for i in range(len(timings_secs)-1)]
    durations.append(durations[-1]) #just recopy the duration of the 2nd to last lyric for the last lyric
    print(durations)

    return indiv_lyrics,durations

def print_lyrics(indiv_lyrics,durations):
    for index,lyric in enumerate(indiv_lyrics):
        duration_per_char=durations[index]/len(lyric)/2
        for c in lyric:
            print(colorama.Fore.YELLOW+c,end="")
            time.sleep(duration_per_char)
        time.sleep(durations[index]/2)
        
        print()
    

indiv_lyrics,durations=parse_lyrics(lyrics1)
os.system('cls')
print_lyrics(indiv_lyrics,durations)

