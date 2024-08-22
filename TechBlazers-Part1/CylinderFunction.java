public class CylinderFunction{

	private double radius;
	private double length;
	private double pi = 3.14159;

   public CylinderFunction(double radius, double length){
	this.radius = radius;
	this.length = length;
   }

   public double computeArea(){
	return pi * (radius * radius);
   }

   public double computeVolume(){
 	return computeArea() * length;
   }
}