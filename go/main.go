package main
// LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!LET'S ALL LOVE LAIN!

import (
	"os"
	"fmt"
	"math/rand"
	"time"
	"errors"
	s "strings"
	"bufio"
	"strconv"
)
const yin  = "--  --"
const yang = "------"

var p = fmt.Println

func castLine(n int) (bool, bool, error) {
	if n == 0 {
		return false, true, nil
	} else if n < 4 {
		return true, false, nil
	} else if n < 9 {
		return true, true, nil
	} else if n < 16 {
		return false, false, nil
	} else {
		return false, false, errors.New("Lain's fucking with you")
	}
}

func stringifyGram(b bool) string {
	if b {
		return yang
	} else {
		return yin
	}
}

func printGrams(gram [6]bool, cgram [6]bool) string {
	format := s.Join([]string{
		"%s     %s",
		"%s     %s",
		"%s --\\ %s",
		"%s --/ %s",
		"%s     %s",
		"%s     %s",
	}, "\n")
	lines := make([]any, 0)
	for idx, _ := range gram {
		lines = append(lines, stringifyGram(gram[idx]))
		lines = append(lines, stringifyGram(cgram[idx]))
	}
	return fmt.Sprintf(format, lines...)
}

func stringifyAsNumber(gram [6]bool) string {
	xs := make([]string, 0)
	for _, b := range(gram) {
		if b {
			xs = append(xs, "1")
		} else {
			xs = append(xs, "0")
		}
	}
	return s.Join(xs, "")
}

func findNumber(gram [6]bool, cgram[6]bool) (int, int, error) {
	f, err := os.Open("./hexagrams.csv")
	if err != nil {
		return -1, -1, err
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)


	gramS := stringifyAsNumber(gram)
	cgramS := stringifyAsNumber(cgram)
	gramN := 0
	cgramN := 0
	for scanner.Scan() {
		text := scanner.Text()
		if s.Contains(text, gramS) {
			numberString := s.Split(text, ",")[0]
			i, err := strconv.Atoi(numberString)
			if err != nil {
				return -1, -1, err
			}
			gramN = i
		} else if s.Contains(text, cgramS) {
			numberString := s.Split(text, ",")[0]
			i, err := strconv.Atoi(numberString)
			if err != nil {
				return -1, -1, err
			}
			cgramN = i
		}
		if cgramN != 0 && gramN != 0 {
			break
		}
	}
	var e error
	if cgramN == 0 || gramN == 0 {
		e = errors.New("couldn't find a gram")
	}
	return gramN, cgramN, e
}

func cast() (string, error) {
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)
	var hexLines [6]bool
	var changeLines [6]bool
	for idx, _ := range hexLines {
		line, change, err := castLine(r1.Intn(16))
		if err != nil {
			return "", err
		}
		hexLines[idx] = line
		changeLines[idx] = change
	}
	hexNumber, changeNumber, err := findNumber(hexLines, changeLines)
	p(hexNumber)
	p(changeNumber)
	return printGrams(hexLines, changeLines), err
}

func main() {
	p("LET'S ALL LOVE LAIN!")
	val, err := cast()
	if err != nil {
		panic(err)
	}
	p(val)
	p("LET'S ALL LOVE LAIN!")
}
