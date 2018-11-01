def forward(x):
  speed = x * 10
  pin0.write_analog(speed)
  pin1.write_analog(speed)

def left(x):
  speed = x * 10
  pin0.write_analog(0)
  pin1.write_analog(speed)

def right(x):
  speed = x * 10
  pin1.write_analog(0)
  pin0.write_analog(speed)

def stop():
  pin0.write_analog(0)
  pin1.write_analog(0)
