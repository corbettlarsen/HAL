pyramidSide = 100;
module button(){
//actual 45.37, 49.57, 38.75
//cylinder actual diameter: 29.88, 
// distance from nut: 7.9
cube([46.4,50.5,39.75]);
translate([23.3,25.25,39.75])
cylinder(20,d=30.88);
}
module pyramid(pSide){
    polyhedron(
    points=[ [pSide,pSide,0],
             [pSide,0,0],
             [0,0,0],
             [0,pSide,0],
             [pSide/2,pSide/2,pSide]  ],
    faces=[ [0,1,4],
            [1,2,4],
            [2,3,4],
            [3,0,4],
            [3,2,1,0] ]
  );
}
difference(){
difference(){
pyramid(pyramidSide);
translate([0,0,47.65])
cube(1000,1000,1000);
}
//these expressions in this translate center the buttons based on the pyramid size.
translate([(pyramidSide-46.4)/2,(pyramidSide-50.5)/2,0])
button();
}
