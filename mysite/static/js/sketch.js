// Flocking
// Daniel Shiffman
// https://thecodingtrain.com/CodingChallenges/124-flocking-boids.html
// https://youtu.be/mhjuuHl6qHM

const flock = [];

let alignSlider, cohesionSlider, separationSlider;

function setup() {
  let canvas = createCanvas(windowWidth, windowHeight);
  canvas.parent("sketch")
  alignSlider = createSlider(0, 2, 1.5, 0.1);
  alignSlider.parent("alignment")
  cohesionSlider = createSlider(0, 2, 1, 0.1);
  cohesionSlider.parent("cohesion")
  separationSlider = createSlider(0, 2, 2, 0.1);
  separationSlider.parent("seperation")
  for (let i = 0; i < 100; i++) {
    flock.push(new Boid());
  }

}

function draw() {
  background(0);
  for (let boid of flock) {
    boid.edges();
    boid.flock(flock);
    boid.update();
    //boid.show();
    boid.render()
  }  
}