package net.talvi.pythonjavabridgedemos;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
import jep.Interpreter;
import jep.JepException;
import jep.SharedInterpreter;
import org.apache.commons.cli.CommandLine;
import org.apache.commons.cli.CommandLineParser;
import org.apache.commons.cli.DefaultParser;
import org.apache.commons.cli.HelpFormatter;
import org.apache.commons.cli.Option;
import org.apache.commons.cli.Options;
import org.apache.commons.cli.ParseException;
import py4j.GatewayServer;

/**
 * A minimal class to demonstrate the use of various Python-Java bridge
 * frameworks. It exposes constructor, a public field, and two simple
 * methods to test Java access from Python scripts. It also has a
 * {@link #main(java.lang.String[]) } method which provides a command-line
 * interface for calling Python scripts from Java using different libraries.
 * 
 * @author pont
 */
public class Main {

    /**
     * A person's name, set in the constructor and used in the
     * {@link #greet(java.lang.String) } method.
     */
    public String name;
    
    /**
     * Instantiates a new Main class with a supplied name.
     * 
     * @param name a person's name to be used for producing greetings
     */
    public Main(String name) {
        this.name = name;
    }
    
    /**
     * Parses command-line arguments. If {@code -jepscript <file>}
     * is passed, {@code <file>} will be run as a Python script using Jep.
     * If {@code -jythonscript <file>} is passed, {@code <file>} will be
     * run as a Python script using Jython.
     * 
     * @param args
     * @throws Exception 
     */
    public static void main(String[] args) throws Exception {
        final Options options = new Options();
        
        options.addOption(Option.builder("jepscript")
            .hasArg().argName("file").desc("run a Python script with Jep")
            .build());
        options.addOption(Option.builder("jythonscript")
            .hasArg().argName("file").desc("run a Python script with Jython")
            .build());
        options.addOption(Option.builder("startpy4jserver")
            .desc("start a Py4J server")
            .build());
        options.addOption(Option.builder("h").longOpt("help").build());

        final CommandLineParser parser = new DefaultParser();
        
        try {
            final CommandLine commandLine = parser.parse(options, args);
            if (commandLine.hasOption("h")) {
                final HelpFormatter formatter = new HelpFormatter();
                formatter.printHelp("pythonjavabridgedemos", "", options,
                        "", true);
                return;
            }
            if (commandLine.hasOption("jepscript")) {
                runJepScript(commandLine.getOptionValue("jepscript"));
            }
            if (commandLine.hasOption("jythonscript")) {
                runJythonScript(commandLine.getOptionValue("jythonscript"));
            }
            if (commandLine.hasOption("startpy4jserver")) {
                startPy4jServer();
            }
        } catch (ParseException ex) {
            System.err.println("Could not parse arguments.\n"
                    + ex.getMessage());
            System.exit(1);
        } 
    }

    /**
     * Runs a specified script using the Jep framework.
     * 
     * @param filename the filename of the script to run
     */
    private static void runJepScript(String filename) {
        try (Interpreter interp = new SharedInterpreter()) {
            interp.set("main", new Main("Jeff"));
            interp.runScript(filename);
        } catch (JepException ex) {
            System.err.println("Jep exception:\n"
                    + ex.getMessage());
            System.exit(1);
        }
    }
    
    /**
     * Runs a specified script using Jython
     * 
     * @param filename the filename of the script to run
     * @throws FileNotFoundException
     * @throws IOException
     * @throws ScriptException 
     */
    private static void runJythonScript(String filename)
            throws FileNotFoundException, IOException, ScriptException {
        final ScriptEngine scriptEngine =
                new ScriptEngineManager().getEngineByName("python");
        scriptEngine.put("main", new Main("Jeff"));
        try (Reader reader = new FileReader(filename)) {
            scriptEngine.eval(reader);
        }
    }

    /**
     * Starts a Py4J server (blocking).
     */
    private static void startPy4jServer() {
        final Main main = new Main("Heliogabalus");
        final GatewayServer server = new GatewayServer(main);
        server.start(false);
    }

    /**
     * Returns the sum of two integers
     * 
     * @param a an integer
     * @param b another integer
     * @return the sum of {@code a} and {@code b}
     */
    public int add(int a, int b) {
        return a + b;
    }
    
    /**
     * Greets the person specified by {@link #name} using a supplied greeting.
     * 
     * @param greeting a greeting
     * @return a string addressing the specified greeting to the person named
     *    in {@link #name}.
     */
    public String greet(String greeting) {
        return greeting + ", " + name + "!";
    }
    
    
}
