    // This program will create a class structure with the superclass being Mammal; three subclasses
    // Class Mammmal: order, name
    // Subclasses: action, sound, and a toString that includes their name, action, sound, and species.
    import java.util.Scanner;

class Mammal {
    String name;
    String species;

    public Mammal(String species, String name) {
        this.species = species;
        this.name = name;
    }


    public String toString() {
        return "the " + this.species + " is named " + this.name + ".";
    }

    public static void main(String[] args) {
        Cow theCow = new Cow("cole");
        System.out.println(theCow.toString());

        Monkey theMonkey = new Monkey("monk");
        System.out.println(theMonkey.toString());

        Wolf theWolf = new Wolf("willy");
        System.out.println(theWolf.toString());
    }
}

class Cow extends Mammal {
    private String action;
    private String sound;
    private String favoriteFood;

    public Cow(String name) {
        super("cow", name);
        this.action = "grazing";
        this.sound = "MOOO!";
        this.favoriteFood = "grass";
    }

    public String getAction() {
        return action;
    }

    public String getSound() {
        return sound;
    }

    public String getFavoriteFood() {
        return favoriteFood;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public void setFavoriteFood(String favoriteFood) {
        this.favoriteFood = favoriteFood;
    }


    public String toString() {
        return super.toString() + " action: " + action + ", sound: " + sound + ", favorite food: " + favoriteFood;
    }
}

class Monkey extends Mammal {
    private String action;
    private String sound;
    private String favoriteFood;

    public Monkey(String name) {
        super("monkey", name);
        this.action = "swinging";
        this.sound = "OHH OHH AHH AHH!";
        this.favoriteFood = "bananas";
    }

   
    public String getAction() {
        return action;
    }

    public String getSound() {
        return sound;
    }

    public String getFavoriteFood() {
        return favoriteFood;
    }

    
    public void setAction(String action) {
        this.action = action;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public void setFavoriteFood(String favoriteFood) {
        this.favoriteFood = favoriteFood;
    }

    public String toString() {
        return super.toString() + " action: " + action + ", sound: " + sound + ", favorite food: " + favoriteFood;
    }
}

class Wolf extends Mammal {
    private String action;
    private String sound;
    private String favoriteFood;

    public Wolf(String name) {
        super("wolf", name);
        this.action = "hunting";
        this.sound = "AWOOOOO!";
        this.favoriteFood = "meat";
    }

    public String getAction() {
        return action;
    }

    public String getSound() {
        return sound;
    }

    public String getFavoriteFood() {
        return favoriteFood;
    }

    
    public void setAction(String action) {
        this.action = action;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public void setFavoriteFood(String favoriteFood) {
        this.favoriteFood = favoriteFood;
    }


    public String toString() {
        return super.toString() + " action: " + action + ", sound: " + sound + ", favorite food: " + favoriteFood;
    }
}
