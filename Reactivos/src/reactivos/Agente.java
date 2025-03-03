
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
        
        int dirRow=0;
        int dirCol=0;


        while(true)
        {
            dirRow = 0; // Reiniciar en cada iteración
            dirCol = 0; // Reiniciar en cada iteración

            casillaAnterior = tablero[i][j];
            
            int direccion = obtenerDireccion(i, j);


            if (direccion == 1){
                dirRow = dirRow + 1;
            } else if (direccion == 2){
                dirRow = dirRow - 1;
            } else if (direccion == 3){
                dirCol = dirCol + 1;
            }else if (direccion == 4){
                dirCol = dirCol - 1;
            }

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

    public int obtenerDireccion(int i, int j) {
        while (true) {
            double random = Math.random();
            if (random >= 0 && random < 0.25) {
                if (!colision(i + 1, j)) {
                    return 1; // Arriba
                }
            } else if (random >= 0.25 && random < 0.5) {
                if (!colision(i - 1, j)) {
                    return 2; // Abajo
                }
            } else if (random >= 0.5 && random < 0.75) {
                if (!colision(i, j + 1)) {
                    return 3; // Derecha
                }
            } else if (random >= 0.75 && random < 1) {
                if (!colision(i, j - 1)) {
                    return 4; // Izquierda
                }
            }
        }
    }


    public boolean colision(int i, int j) {
        // Verifica si la posición está fuera de los límites del tablero o si hay un obstáculo (1)
        if (i < 0 || i >= matrix.length || j < 0 || j >= matrix.length || matrix[i][j] == 1) {
            return true; // Hay colisión
        }
        return false; // No hay colisión
    }
    
    public void entregarSample(){

    }
    
}
