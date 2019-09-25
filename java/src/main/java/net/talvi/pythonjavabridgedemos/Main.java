package net.talvi.pythonjavabridgedemos;

public class Main {
    
    public String name;
    
    public Main(String name) {
        this.name = name;
    }
    
    public int add(int a, int b) {
        return a + b;
    }
    
    public String greet(String greeting) {
        return greeting + ", " + name + "!";
    }
    
}
