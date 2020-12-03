import time
import sys


#here is the animation
def animate():
    character=['/','-','\\','-']
    percentage=0
    for _ in range(1):
        # for cha in character:
        percentage=percentage+10
        sys.stdout.write(f'\r Decrypting ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████░░░░░░░░░░░░░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████████░░░░░░░░░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████████████░░░░░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████████████████░░░░░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████████████████████░░░░░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████████████████████████░░░░ {percentage}')
        time.sleep(.1)
        percentage = percentage + 10
        sys.stdout.write(f'\r Decrypting ████████████████████████████████████████ {percentage}')
        time.sleep(.1)




