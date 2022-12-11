########################################################################
# ECE5504 ....
########################################################################

CC := riscv64-unknown-elf-gcc
OBJDUMP := riscv64-unknown-elf-objdump
CFLAGS := -O0 -std=gnu11 -Wall -specs=htif_nano.specs

# OBJECTS = mat-mul-add1 mat-mul-add2 mat-mul-add3 mat-mul-add4 mat-mul-add5 mat-mul-add6 mat-mul-add7 mat-mul-add8 mat-mul-add9 mat-mul-add10
OBJECTS = mat-mul-add5x5 mat-mul-add10x10  mat-mul-add15x15  mat-mul-add20x20  mat-mul-add25x25  mat-mul-add30x30  
all: $(OBJECTS)

$(OBJECTS): %: %.c
	$(CC) $(CFLAGS) -march=rv64g -DSIZE=32 -o $@.riscv $< trap.c
	$(OBJDUMP) -d -M no-aliases $@.riscv > $@.dump

dump: mat-mul-add.riscv
	$(OBJDUMP) -d -M no-aliases $< > $@

.PHONY: clean
clean:
	rm -f -- *.riscv *.o *.dump

.SUFFIXES: # Disable built-in suffix rules
