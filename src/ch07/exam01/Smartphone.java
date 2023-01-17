package ch07.exam01;

public class Smartphone extends Phone {
	public Smartphone(String model, String color) {
		this.model = model;
		this.color = color;
		
		System.out.println( "public Smartphone(String model, String color) "+this.model + this.color);
	}
}
