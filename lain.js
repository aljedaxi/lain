'use strict'
let expect = require('chai').expect;

class Line {
	constructor(line, change) {
		this.line = line;
		this.change = change;
	}
}

function rand_in_16() {
	let min = 0;
	let max = 16;
	return Math.floor(
		Math.random() * (max - min) + min
	);
}

function cast_line(num) {
	if (num == 0) {
		return new Line(0,1);
	} else if ((num > 0) && (num < 4)){
		return new Line(1,0);
	} else if ((num > 3) && (num < 9)){
		return new Line(1,1);
	} else if ((num > 8) && (num < 16)){
		return new Line(0,0);
	} else {
		console.log(num);
		throw "Lain's fucking with you.";
	}
}

function gen_grams(question) {
	function* caster(n_lines) {
		for(let i = 0; i < n_lines; i++){
			yield cast_line(rand_in_16());
		}
	}

	let gram = [];
	let cgram = [];

	for(let line of caster(6)){
		gram.push(line.line);
		cgram.push(line.change);
	}

	gram.reverse();
	cgram.reverse();

	return [gram, cgram];
}

function main(
	question,
	yin="- -",
	yang="---",
	lain_csv="lain.csv",
	bagua_csv="bagua.2.csv",
	browsing=true,
	//websitefun=the_iching,
	//browser="qutebrowser",
) {
	function print_grams(gram, cgram) {
			function t(line) {
				switch(line) {
					case 0:
						return yin;
						break;
					case 1:
						return yang;
						break;
				}
			}

			let return_string = 
				`${t(gram[0])}     ${t(cgram[0])}\n` +
				`${t(gram[1])}     ${t(cgram[1])}\n` +
				`${t(gram[2])} __\\ ${t(cgram[2])}\n` +
				`${t(gram[3])} --/ ${t(cgram[3])}\n` +
				`${t(gram[4])}     ${t(cgram[4])}\n` +
				`${t(gram[5])}     ${t(cgram[5])}\n`

			return return_string;
	}
	let gram = [];
	let cgram = [];
	[gram, cgram] = gen_grams(question);
	let formatted_gram = print_grams(gram, cgram);

	return formatted_gram;
}

let question = process.argv[process.argv.length - 1];
console.log(
	main(question)
);

/*
describe('line', function() {
	it('should contain a line and changed line', function() {
		let line = new Line(1, 0);
		expect(line).to.eql({
			line: 1,
			change: 0,
		});
	});
});

describe('cast_line', function() {
	it('should handle 9', function() {
		let at9 = cast_line(9);
		expect(at9).to.eql({
			line: 0,
			change: 0,
		});
	});
});
*/
