########################################################################
# ECE5504 ....
########################################################################

CC := riscv64-unknown-elf-gcc
OBJDUMP := riscv64-unknown-elf-objdump

CFLAGS := -O0 -std=gnu11 -Wall -specs=htif_nano.specs

all:
	max-path-sum
	dump

compile: max-path-sum.c trap.c
	$(CC) $(CFLAGS) -march=rv64g -DSIZE=32 -o max-path-sum.riscv $< trap.c


dump: max-path-sum.riscv
	$(OBJDUMP) -d -M no-aliases $< > $@

.PHONY: clean
clean:
	rm -f -- *.riscv *.o *.dump

.SUFFIXES: # Disable built-in suffix rules
