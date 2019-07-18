#!/usr/bin/env python3


"""Voice Control of RoboKar"""
import argparse
import locale
import logging

from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
#import aiy.voice.tts 


def get_hints(language_code):
    if language_code.startswith('en_'):
        return ('linear','angular','stop','full speed','forward','back','fast','slow',
                'goodbye')
    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', args.language)
    hints = get_hints(args.language)
    client = CloudSpeechClient()
    with Board() as board:
        while True:
            if hints:
                logging.info('Say something, e.g. %s.' % ', '.join(hints))
            else:
                logging.info('Say something.')
            text = client.recognize(language_code=args.language,
                                    hint_phrases=hints)
            if text is None:
                logging.info('You said nothing.')
                continue

            logging.info('You said: "%s"' % text)
            text = text.lower()
            if 'turn on the light' in text:
                board.led.state = Led.ON
            elif 'turn off the light' in text:
                board.led.state = Led.OFF
            elif 'blink the light' in text:
                board.led.state = Led.BLINK
            elif 'linear' in text:
                # Remove "repeat after me" from the text to be repeated
                linear_velocity = text.replace('linear', '', 1)
                #aiy.voice.tts.say(to_repeat)
                print('Linear Velocity: ',float(linear_velocity))
            elif 'angular' in text:
                # Remove "repeat after me" from the text to be repeated
                angular_velocity = text.replace('angular', '', 1)
                #aiy.voice.tts.say(to_repeat)
                print('Angular Velocity: ',float(angular_velocity))
 
            elif 'goodbye' in text:
                break

if __name__ == '__main__':
    main()