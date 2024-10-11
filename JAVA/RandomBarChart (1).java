import javax.swing.*;
// import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.geom.Line2D;
import java.util.Random;

public class RandomBarChart extends JPanel {
    @Override
    public void paintComponent(Graphics g) {
        int red, green, blue;
        Line2D.Double line;
        Random rand = new Random();

        // Set dimensions based on smaller of height or width so chart always fully displays
        // This also makes chart adjust to  size of window
        int maxDimension = Math.min(this.getHeight(), this.getWidth());
        int cellSize = maxDimension/10;

        // Initialize 2D graphics component
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g.create();

        // Draw 10x10 grid using rectangles
        for (int x = 0; x < 10; x++) {
            for (int y = 0; y < 10; y++) {
                g2d.drawRect((x * cellSize), (y * cellSize), cellSize, cellSize);
            }
        }

        // Draw 10 bars between cells
        for (int x = 0; x < 10; x++) {
            // Randomize RGB input
            red = rand.nextInt(256);
            green = rand.nextInt(256);
            blue = rand.nextInt(256);
            g2d.setStroke(new BasicStroke(10f));
            g2d.setColor(new Color(red, green, blue));

            // x values offset by half of cell width
            // Using (cellSize * 10) instead of height so bars start at bottom of chart instead of bottom of window
            // y values offset by 5 to account for consistent 5 pixel error due to integer rounding
            line = new Line2D.Double((x * cellSize) + (cellSize/2), (cellSize*10) - 5, (x * cellSize) + (cellSize/2), rand.nextDouble((cellSize*10) - 5));
            g2d.draw(line);
        }

        g2d.dispose();
    }

    public static void main(String[] args) {

        JButton redrawButton;
        RandomBarChart gPane;

        // Create frame
        JFrame frame = new JFrame("Random Bar Chart");
        frame.setLayout(new BorderLayout());

        // Initialize components

        redrawButton = new JButton("Redraw");
        gPane = new RandomBarChart();
        gPane.setPreferredSize(new Dimension(300, 300)); // Starting size

        // Add button event where repaint() clears canvas and recalls paintComponent()
        redrawButton.addActionListener(e -> gPane.repaint());

        /* Alternative padding approach

        JPanel borderPanel = new JPanel();
        borderPanel.setBorder(new EmptyBorder(50, 50, 50, 50));
        borderPanel.add(gPane);

           Then add borderPanel to frame instead of gPane */

        // Add components with layout placements
        frame.add(gPane, BorderLayout.CENTER);
        frame.add(redrawButton, BorderLayout.SOUTH);

        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE); // delete when window is closed
        frame.pack();   // Resize to minimum size that fits components
        frame.setVisible(true);
    }
}
