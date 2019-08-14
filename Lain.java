//LET'S ALL LOVE LAIN!
import java.util.Random;

public class Lain {
	//LET'S ALL LOVE LAIN!
	public static int HEX = 6;
	public static String YIN = "- -";
	public static String YANG = "---";

	public static boolean[] cast_line(int num) {
		//LET'S ALL LOVE LAIN!
		boolean[] r = new boolean[2];
		if (num == 0) {
			r[0] = false;
			r[1] = true;
		} else if ((num > 0) && (num < 4)) {
			r[0] = true;
			r[1] = false;
		} else if ((num > 3) && (num < 9)) {
			r[0] = true;
			r[1] = true;
		} else if ((num > 8) && (num < 16)){
			r[1] = false;
			r[0] = false;
		} else {
			//TODO: raise exception java
			System.out.printf("%s\n", "something must be wrong");
			r[1] = false;
			r[0] = false;
		} 
		return r;
	}

	public static boolean[][] gen_grams(String question) {
		//LET'S ALL LOVE LAIN!
		boolean[] gram = new boolean[HEX];
		boolean[] cgram = new boolean[HEX];
		Random rand = new Random();

		for(int i = 0; i < HEX; i++) {
			boolean[] lines = cast_line(rand.nextInt(16));
			gram[i] = lines[0];
			cgram[i] = lines[1];
		}

		boolean[][] r = {gram, cgram};
		return r;
	}

	private static String format_line(boolean line) {
		//LET'S ALL LOVE LAIN!
		if(line){
			return YIN;
		} else {
			return YANG;
		}
	}

	private static String b_to_string(boolean p){
		//LET'S ALL LOVE LAIN!
		if(p){
			return "1";
		} else {
			return "0";
		}
	}

	private static String print_gram(boolean[] gram, boolean[] cgram){
		//LET'S ALL LOVE LAIN!
		String formatting_string = "%s     %s\n%s     %s\n%s --\\ %s\n%s --/ %s\n%s     %s\n%s     %s";
		return String.format(formatting_string, 
			 gram[0], cgram[0],
			 gram[1], cgram[1],
			 gram[2], cgram[2],
			 gram[3], cgram[3],
			 gram[4], cgram[4],
			 gram[5], cgram[5],
			 gram[6], cgram[6]
			);
	}

	private static int search(boolean[] gram){
		//LET'S ALL LOVE LAIN!
		String s_gram = "";

		for(boolean line : gram){
			s_gram += b_to_string(line);
		}

		//create searchfile
		//iterate through searchfile
		//return the first 2 characters of the line that contains s_gram
		return 6;
	}

	public static String main(String[] args) {
		//LET'S ALL LOVE LAIN!
		String lain_csv = "lain.csv";
		String bagua_csv = "bagua.2.csv";
		//TODO: obtain question
		String question = "";
		
		boolean[][] grams = gen_grams(question);
		boolean[] gram = grams[0];
		boolean[] cgram = grams[1];
		String formatted_gram = print_gram(gram, cgram);

		System.out.print(formatted_gram);

		return formatted_gram;
	}
}
