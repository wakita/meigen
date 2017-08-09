CC            := icpc
LD            := icpc


# ----------------------------------------
# Using pkg-config (see README.txt):

PKG_CONFIG_PATH := /home/3/wakita-k-aa/lib/pkgconfig

MAGMA_CFLAGS  := $(shell pkg-config --cflags magma)
MAGMA_LIBS    := $(shell pkg-config --libs   magma)

CNPY_CFLAGS   := $(shell pkg-config --cflags cnpy)
CNPY_LIBS     := $(shell pkg-config --libs   cnpy)


CFLAGS        := -Wall $(MAGMA_CFLAGS) $(CNPY_CFLAGS)
LDFLAGS       := -Wall $(MAGMA_LIBS)   $(CNPY_LIBS)


# ----------------------------------------

all: eigen

clean:
	-rm -f example1 *.o


# ----------------------------------------

%.o: %.cpp
	echo $(CFLAGS)
	$(CC) $(CFLAGS) -c -o $@ $<

eigen: eigen.o
	$(LD) $(LDFLAGS) -o $@ $^
