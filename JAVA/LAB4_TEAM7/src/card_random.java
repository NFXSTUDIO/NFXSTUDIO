import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import java.util.Random;
import javax.sound.sampled.*;

public class card_random extends JFrame {

    public card_random() {
        // constant
        int WIDTH = 1200;
        int HEIGHT = 750;
        int sizeX = WIDTH / 15;
        int sizeY = (HEIGHT - 80) / 5;
        Clip sound = null;

        //Creating the frame
        String[] array = getDeckOfCards();
        JFrame frame = new JFrame();
        frame.setTitle("Card randomizer V1.0 TEAM7");
        frame.setSize(WIDTH, HEIGHT);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setIconImage(Toolkit.getDefaultToolkit().getImage("imgs/logo_app.png"));

        //Creating the panel
        JPanel panel = new JPanel(new GridBagLayout());
        panel.setBackground(new Color(16,108,4));
        GridBagConstraints constraints = new GridBagConstraints();

        try {
            AudioInputStream audioInputStream = AudioSystem.getAudioInputStream(new File("sound/card.wav")); // Replace "sound.wav" with your sound file path
            sound = AudioSystem.getClip();
            sound.open(audioInputStream);
        } catch (Exception ex) {
            ex.printStackTrace();
        }

        // function to create button and image
        create_img(panel,constraints,array,sizeX,sizeY);
        create_button(panel,frame,constraints,array,sizeX,sizeY,sound);
    }

    public static void create_button(JPanel panel,JFrame frame,GridBagConstraints constraints,String[] array, int sizeX, int sizeY,Clip sound) {

        // Purpose : Creates a button and adds it to the specified JPanel within a JFrame.
        // IN : - panel: The JPanel where the button will be added.
        //      - frame: The JFrame that contains the JPanel.
        //      - constraints: GridBagConstraints object used to specify the button's position and size within the JPanel.
        //      - array: A String array (likely used for data storage or manipulation within the button's action).
        //      - sizeX: The width of the button.
        //      - sizeY: The height of the button.

        JButton button = new JButton("Shuffle the cards");

        //Constraints
        GridBagConstraints buttonConstraints = new GridBagConstraints();
        buttonConstraints.gridx = 0;
        buttonConstraints.gridy = 4;
        buttonConstraints.gridwidth = GridBagConstraints.REMAINDER;
        buttonConstraints.fill = GridBagConstraints.BOTH;
        buttonConstraints.weightx = 1;
        buttonConstraints.weighty = 1;

        //Add action to the button
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                btn_action(frame, panel, constraints, array,sizeX,sizeY,sound);
            }
        });

        //Add to the panel
        panel.add(button, buttonConstraints);
        frame.add(panel);
        frame.setVisible(true);
    }

    public static void create_img(JPanel panel,GridBagConstraints constraints,String[] array,int sizeX,int sizeY){

        // Purpose: Creates and adds image labels to a JPanel using GridBagLayout.
        // IN:  - panel: The JPanel where the image labels will be added.
        //      - constraints: GridBagConstraints object used to specify the position and size of each image label within the JPanel.
        //      - array: A String array containing file names (likely with the ".png" extension) or image paths relative to the "imgs/" directory.
        //      - sizeX: The desired width of the scaled images.
        //      - sizeY: The desired height of the scaled images.

        //Constant to see all the array
        int imageIndex = 0;

        //Loop
        for (int row = 0; row < 4; row++) {
            for (int col = 0; col < 13; col++) {
                try {
                    String filename = "imgs/" + array[imageIndex] + ".png";
                    BufferedImage img = ImageIO.read(new File(filename));
                    Image scaledImage = img.getScaledInstance(sizeX, sizeY, Image.SCALE_SMOOTH);
                    ImageIcon icon = new ImageIcon(scaledImage);
                    JLabel label = new JLabel(icon);
                    panel.add(label);
                    constraints.gridx = col;
                    constraints.gridy = row;
                    constraints.fill = GridBagConstraints.BOTH;
                    constraints.weightx = 1;
                    constraints.weighty = 1;
                    panel.add(label, constraints);
                    imageIndex++;
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public static void btn_action(JFrame frame,JPanel panel,GridBagConstraints constraints,String[] array,int sizeX,int sizeY,Clip sound){

        // Purpose: Handles the action triggered by the button click.
        // IN:  - frame: The JFrame containing the JPanel.
        //      - panel: The JPanel to be cleared and refilled.
        //      - constraints: GridBagConstraints object used for positioning components within the JPanel.
        //      - array: A String array containing image filenames.
        //      - sizeX: The desired width of the scaled images.
        //      - sizeY: The desired height of the scaled images.

        //Update the panel
        panel.removeAll(); // Supprime tous les composants du panel
        panel.revalidate(); // Valide à nouveau la disposition
        panel.repaint(); // Redessine le panel

        playSound(sound);
        //Make a shuffle and show the new position
        shuffle(array);
        create_img(panel,constraints,array,sizeX,sizeY);
        create_button(panel,frame,constraints,array,sizeX,sizeY,sound);
    }

    public static void shuffle(String[] stringList){

        // Purpose: Randomly shuffles the elements of a given string array.
        // IN:    - stringList: The string array to be shuffled.

        Random r = new Random();

        //Loop
        for(int x = 0; x < stringList.length; x++){
            int randomPos = r.nextInt(stringList.length);
            String temp = stringList[x];
            stringList[x] = stringList[randomPos];
            stringList[randomPos] = temp;
        }
    }

    public static String[] getDeckOfCards(){

        // Purpose: Creates and returns a string array representing a standard deck of 52 playing cards.
        // OUT: String[] - An array of 52 strings, representing the cards in the deck.

        String[] cards = new String[52];

        //set list of suits
        String[] suits = {"hearts","spades","clubs","diamonds"};

        //make list of card names
        for(int x = 0; x < 4; x++) {
            cards[x * 13] = "ace_of_" + suits[x];
            for (int y = 1; y < 10; y++) {
                cards[x * 13 + y] = (y + 1) + "_of_" + suits[x];
            }
            cards[x * 13 + 10] = "jack_of_" + suits[x] + "2";
            cards[x * 13 + 11] = "queen_of_" + suits[x] + "2";
            cards[x * 13 + 12] = "king_of_" + suits[x] + "2";
        }
        return cards;
    }

    public static void playSound(Clip sound) {
        if (sound != null) {
            sound.start();
        }
    }

    public static void main(String[] args) {
        new card_random();
    }
}