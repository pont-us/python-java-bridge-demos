package net.talvi.pythonjavabridgedemos;

import jep.Interpreter;
import jep.JepException;
import jep.SharedInterpreter;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;


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
    
    public static void runJepScript(String filename) {
        try (Interpreter interp = new SharedInterpreter()) {
            interp.runScript(filename);
        } catch (JepException ex) {
            System.err.println("Jep exception:\n"
                    + ex.getMessage());
            System.exit(1);
        }
    }
    
    public static void main(String[] args) {
        final Options options = new Options();
        
        options.addOption(Option.builder("jepscript")
            .hasArg().argName("file").desc("run a Python script with Jep")
            .build());
        final CommandLineParser parser = new DefaultParser();
        
        try {
            final CommandLine commandLine = parser.parse(options, args);
            if (commandLine.hasOption("jepscript")) {
                runJepScript(commandLine.getOptionValue("jepscript"));
            }
        } catch (ParseException ex) {
            System.err.println("Could not parse arguments.\n"
                    + ex.getMessage());
            System.exit(1);
        } 
    }
}
