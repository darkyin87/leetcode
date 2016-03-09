/*
The Question:



The most common word greater than 4 characters in the play Macbeth is ŒMacbeth¹ (Imagine that!). It appears 285 times.
Your challenge is to write a program that will read the Œmacbeth.txt¹ file and find the SECOND MOST COMMON word greater than 4 characters in length in the play Macbeth.
To get the answer correct, you must account for the fact that the word is sometimes followed by the following punctuation:
Comma, Period, Question Mark, Colon, Semi-colon, Exclamation Mark



To complete this challenge successfully your program must:

1. Read the file Œmacbeth.txt¹.

2. Eliminate all words that are 4 characters or less.

3. Account for words that are followed by punctuation.

4. Output the 2nd most common word and the number of times it appears.
 */

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Stream;
import static java.util.function.Function.identity;
import static java.util.stream.Collectors.*;
import java.util.Comparator;
import java.util.Optional;

public class WordCount {
    Map<String, Long> words;

    public WordCount(Path path) throws IOException {
        try (Stream<String> lines = Files.lines(path)) {
            this.words = countWords(removePunc(lines));
        }
    }

    private static Optional<Map.Entry<String, Long>> findMostCommonWord(Map<String, Long> wordMap) {
        Comparator<Map.Entry<String, Long>> byValue = (entry1, entry2) -> entry1.getValue().compareTo(entry2.getValue());

        Optional<Map.Entry<String, Long>> val = wordMap
                .entrySet()
                .stream()
                .sorted(byValue.reversed())
                .findFirst();

        return val;
    }

    private static Stream<String> removePunc(Stream<String> stream) {
        return stream.map(s -> s.replaceAll("\t", " ")
                .replaceAll("[^a-zA-Z ]", "")
                .replaceAll("\\s+", " "));
    }

    private static Map<String, Long> countWords(Stream<String> stream) {
        return stream.map(String::toLowerCase)
                .map(s -> s.split(" "))
                .flatMap(Arrays::stream)
                .filter(s -> s.length() > 4)
                .filter(s -> !s.equals("macbeth"))
                .collect(groupingBy(identity(), counting()));
    }

    public Optional<Long> count(String word) {
        return Optional.ofNullable(words.get(word));
    }

    public void printWords() {
        System.out.println(Arrays.toString(words.entrySet().toArray()));
    }

    public static void main(String[] args) {
        final Path path = FileSystems.getDefault().getPath(args[0]);
        WordCount wc = null;
        try {
            wc = new WordCount(path);
        } catch (IOException e) {
            System.out.println("No file found :(");
        }

        wc.printWords();
        System.out.println(wc.findMostCommonWord(wc.words));

    }
}
