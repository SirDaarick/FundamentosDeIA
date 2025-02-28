
package reactivos;

import java.util.Random;
import javax.swing.ImageIcon;
import javax.swing.JLabel;

/**
 *
 * @author macario
 */
public class Agente extends Thread
{
    private final String nombre;
    private int i;
    private int j;
    private final ImageIcon icon;
    private final int[][] matrix;
    private final JLabel tablero[][];
    
    private JLabel casillaAnterior;
    Random aleatorio = new Random(System.currentTimeMillis());
    
    public Agente(String nombre, ImageIcon icon, int[][] matrix, JLabel tablero[][])
    {
        this.nombre = nombre;
        this.icon = icon;
        this.matrix = matrix;
        this.tablero = tablero;

        
        this.i = aleatorio.nextInt(matrix.length);
        this.j = aleatorio.nextInt(matrix.length);
        tablero[i][j].setIcon(icon);        
    }
    
    @Override
    public void run()
    {
        
        int dirRow=1;
        int dirCol=1;


        while(true)
        {

            casillaAnterior = tablero[i][j];
               
            if(i > matrix.length-2 && dirRow == 1) dirRow=-1;
            if(i < 1 && dirRow==-1) dirRow=1;

            if(j > matrix.length-2 && dirCol ==1) dirCol=-1;
            if(j < 1 && dirCol==-1) dirCol=1;
                            
            i=i+dirRow;
            j=j+dirCol;
                            
            actualizarPosicion();
                
            try
            {
               sleep(100+aleatorio.nextInt(100));
            }
            catch (InterruptedException ex)
            {
                ex.printStackTrace(System.out);
            }
        }

                      
    }
    
    public synchronized void actualizarPosicion()
    {
        casillaAnterior.setIcon(null); // Elimina su figura de la casilla anterior
        tablero[i][j].setIcon(icon); // Pone su figura en la nueva casilla
        System.out.println(nombre + " in -> Row: " + i + " Col:"+ j);              
    }
    
}
