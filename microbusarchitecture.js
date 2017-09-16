process.stdin.resume();
process.stdin.setEncoding('utf8');
process.stdin.on('data', function (text) {
  if (text === 'quit\n') {
    done();
  }
  if(text.indexOf('\n')) {
    const lines = text.split('\n');
    lines.forEach((line) => {
      // prep variable
      const inputBinary = line.split('#')[0].trim();
      const inputDecimal = Number('0b' + inputBinary);
      //console.log('decimal' + inputDecimal);
      //console.log('binary' + inputBinary);
      if(!isNaN(inputDecimal)) {
        cpu.process(inputDecimal);
      }
    });
  }
});

function done() {
  process.exit();
}

let dict = {
    '00000001': 'initialize',
    '00000010': 'set',
    '00000100': 'save',
    '00000101': 'multiply',
    '00000110': 'print_numeric'
}

let registers = {
  'reg0': 0,
  'reg1': 0,
  'reg2': 0,
  'reg3': 0,
}

// initialize function
function initialize(registers) {
  for (key in Object.keys(registers)) {
    registers[key] = 0;
  }
}

// turn binary to decimal
function binToDec(binaryStr) {
  return parseInt(binaryStr, 2);
}

