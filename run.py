import subprocess
from zhipuai import ZhipuAI
import time
import logging
import sys, os

if not os.path.exists('apikey.txt'):
    print("Please put your ChatGLM API key in apikey.txt")
    exit(1)
with open('apikey.txt') as f:
    apikey=f.read().strip()
    client = ZhipuAI(api_key=apikey)

logging.basicConfig(filename="airadio.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

def get_music_info():
    output = subprocess.getoutput("./nowplaying-cli get title album artist")
    return output.split("\n")

def get_desc(title, album, artist, dummy=False):
    logger.info(f"PREPARE AI RESPONSE [{title} | {album} | {artist}]")
    if dummy or len(str(title))<2:
        time.sleep(1)
        return "观众朋友，欢迎收听古典音乐频道。让我们开始吧！"
    else:
        prompt = f"你是一个古典音乐电台的主持人，下面你要播放的是{artist}的{title}({album})，请解说一下这首作品。请用一两分钟介绍这首作品本身，比如创作背景、作曲手法等等，一定不要讲任何空洞的废话，要尽可能讲音乐专业的内容。解说词里一定不可以有任何外文。你必须只提供有效真实的信息，不要任何起承转合的套话。"
        logger.info(f"PROMPT: {prompt}")
        
        response = client.chat.completions.create(
            model="glm-4",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            top_p=0.7,
            temperature=0.95,
            max_tokens=1024,
            stream=False,
        )
        res = str(response.choices[0].message.content)
        logger.info(f"AI RESPONSE: {res}")
        return res

def speak(cntt):
    with open('/tmp/ai_radio_tmp_say.txt','w') as f:
        f.write(cntt)
    subprocess.run("say -f /tmp/ai_radio_tmp_say.txt", shell=True)
    time.sleep(0.2)
    os.unlink('/tmp/ai_radio_tmp_say.txt')
    
def set_music_play():
    subprocess.run("./nowplaying-cli play", shell=True)
    time.sleep(0.1)
    logger.info(f"PLAY")

def set_music_pause():
    subprocess.run("./nowplaying-cli pause", shell=True)
    logger.info(f"PAUSE")

def set_music_next():
    subprocess.run("./nowplaying-cli next", shell=True)
    logger.info(f"NEXT")

def get_music_time_left():
    elps, dura = subprocess.getoutput("./nowplaying-cli get elapsedTime duration").split('\n')
    elps = float(elps)
    dura = float(dura)
    return dura-elps

def get_music_time_elapsed():
    try:
        elps = float(subprocess.getoutput("./nowplaying-cli get elapsedTime"))
    except:
        elps = 0
    return elps

speak_flag=True
first_speak_dummy=True
last_elapse=0
while True:
    if speak_flag:
        try:
            # if this song is to end, let's jump to the next song but stop at the 
            # very beginning and don't let the first beat be played
            # now lets start the voiceover
            if get_music_time_left()<1:
                set_music_next()
            set_music_pause()
            title, album, artist = get_music_info()

            # TODO: AI needs time to respond, so in this short period, something
            # such as cheers can be added to avoid the silence
            say_content = get_desc(title, album, artist, first_speak_dummy)
            speak(say_content)
            set_music_play()
            first_speak_dummy = False
            speak_flag = False
        except Exception as e:
            print(e)

    else:
        time.sleep(0.2)
        try:
            if get_music_time_left()<1:
                speak_flag = True
        except:
            pass