
class Particle(object) :
    
    def __init__ (self, position, velocity, mass):
        self.pos = position
        self.vel = velocity
        self.mass = mass
        self.acc = PVector(0,0)
        
    def position (self) :
        return(self.pos)
    
    def velocity (self) :
        return(self.vel)
    
    def get_mass (self) :
        return(self.mass)
    
    def write_acc (self, accvec) :
        self.acc = accvec
        
    def update_status (self) :
        x,y=self.pos.x,self.pos.y
        (self.pos).add(self.vel)
        (self.vel).add(self.acc)
        stroke(255)
        strokeWeight(self.mass*0.1)
        line(self.pos.x, self.pos.y, x, y)
        
        

def accel (star) :
    accref = PVector(0,0)
    for other_star in set(stars)-{stars[stars.index(star)]} :
        r_vec = PVector.sub(star.position(), other_star.position())
        acc_mag = other_star.get_mass() * ((r_vec.mag())**-1)
        r_vec.normalize()
        accref.add(PVector.mult(r_vec, -0.1*acc_mag))
    return accref
        
        
   
stars = []
for i in range (10) :
    position = PVector(randomGaussian()*70+1920/2,randomGaussian()*70+1080/2)
    vec = PVector.sub(position, PVector(1920/2, 1080/2))
    vectemp = vec
    vec.rotate(HALF_PI+randomGaussian()*0.2)
    vec.setMag((70+randomGaussian()*5)*(vectemp.magSq())**-1)
    star = Particle( position, vec, random(random(10),10))
    stars.append(star)
    
    

def setup () :
    size(1920,1080)
    background(50)

def draw () :
    noStroke()
    fill(50, 50, 50, 50)
    rect(0, 0, width, height)
    fill(50, 50, 50, 255)
    rect(0, 0, 200, 50)
    fill(200, 200)
    textSize(20)
    text('#Epoch.'+str(frameCount), 20, 20, 200, 50)
    for star in stars :
        star.write_acc(accel(star))
        star.update_status()
    saveFrame("frames/######.png")
