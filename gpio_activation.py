import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.cleanup() 