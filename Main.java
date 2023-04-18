
// it doesnt actually use this java class btw.

package net.kealands;

import javax.imageio.ImageIO;

import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;


public class Main {

    private final static HashSet<ImagePoint> points = new HashSet<>(Set.of(
            new ImagePoint(152, 185), new ImagePoint(160, 148), new ImagePoint(178, 116),
            new ImagePoint(201, 82), new ImagePoint(223, 65), new ImagePoint(277, 46),
            new ImagePoint(317, 41), new ImagePoint(355, 43), new ImagePoint(392, 60),
            new ImagePoint(423, 85), new ImagePoint(451, 116), new ImagePoint(467, 151), new ImagePoint(472, 190)
    ));

    private final static HashMap<String, Integer> amount = new HashMap<>();

    public static void start() {
        BufferedImage img = null;
        try {
            img = ImageIO.read(new File("C:\\Users\\Beary\\Desktop\\github\\RustWheel\\RustWheelBot\\tmp.png"));
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        for(int i = 0; i < points.size(); i++) {
            ImagePoint p = points.stream().toList().get(i);
            Color oldColor = new Color(img.getRGB(p.x, p.y));
            Color color = new Color(img.getRGB(p.x, p.y));
            color = manipulateColour(color);
            //System.out.println(i + ": " + p.x + ", " + p.y + " = NOW:" + color.toString().replace("java.awt.Color", "") + " WAS: " + oldColor.toString().replace("java.awt.Color", ""));
            String name = closestColorName(color.getRed(), color.getGreen(), color.getBlue());
            if(!amount.containsKey(name))
                amount.put(name, 1);
            else amount.put(name, amount.get(name) + 1);

            //System.out.println(color.toString());
        }
        //amount.forEach((s, integer) -> System.out.println(s + ": " + integer));
    }

    private static Color manipulateColour(Color color) {

        float[] hsv = new float[3];
        Color.RGBtoHSB(color.getRed(), color.getGreen(), color.getBlue(), hsv);

        hsv[2] = 1.0f;

        int rgb = Color.HSBtoRGB(hsv[0], hsv[1], hsv[2]);
        return new Color(rgb);
    }
    public static String closestColorName(int r, int g, int b) {
        // Define the ranges for each color in the RGB color space
        int[][] colorRanges = {
                {255, 118, 58},    // Red
                {255, 255, 62},  // Yellow
                {91, 255, 67},    // Green
                {255, 0, 245}, // Pink
                {75, 159, 255}     // Blue
        };

        // Find the color with the smallest distance to the given RGB values
        int minDistance = Integer.MAX_VALUE;
        String closestColorName = "";
        for (int i = 0; i < colorRanges.length; i++) {
            int[] colorRange = colorRanges[i];
            int distance = (r - colorRange[0]) * (r - colorRange[0]) +
                    (g - colorRange[1]) * (g - colorRange[1]) +
                    (b - colorRange[2]) * (b - colorRange[2]);
            if (distance < minDistance) {
                minDistance = distance;
                closestColorName = getColorName(i);
            }
        }

        return closestColorName;
    }

    // Helper method to get the color name from an index
    public static String getColorName(int index) {
        String[] colorNames = {"Red", "Yellow", "Green", "Pink", "Blue"};
        return colorNames[index];
    }

    public static int getRed() {
        return amount.getOrDefault("Red", 0);
    }
    public static int getBlue() {
        return amount.getOrDefault("Blue", 0);
    }
    public static int getPink() {
        return amount.getOrDefault("Pink", 0);
    }

    public static void main(String[] args) throws IOException {
        start();
    }

    public static class ImagePoint {

        public int x;
        public int y;

        public ImagePoint(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

}