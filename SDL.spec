#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL
Version  : 1.2.15
Release  : 11
URL      : https://www.libsdl.org/release/SDL-1.2.15.tar.gz
Source0  : https://www.libsdl.org/release/SDL-1.2.15.tar.gz
Source99 : https://www.libsdl.org/release/SDL-1.2.15.tar.gz.sig
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: SDL-bin
Requires: SDL-lib
Requires: SDL-doc
BuildRequires : alsa-lib-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : nasm-bin
BuildRequires : pkgconfig(32alsa)
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32glu)
BuildRequires : pkgconfig(32ice)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcb-glx)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xrandr)
Patch1: SDL-1.2.15-const_XData32.patch

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the SDL package.
Group: Binaries

%description bin
bin components for the SDL package.


%package dev
Summary: dev components for the SDL package.
Group: Development
Requires: SDL-lib
Requires: SDL-bin
Provides: SDL-devel

%description dev
dev components for the SDL package.


%package dev32
Summary: dev32 components for the SDL package.
Group: Default
Requires: SDL-lib32
Requires: SDL-bin
Requires: SDL-dev

%description dev32
dev32 components for the SDL package.


%package doc
Summary: doc components for the SDL package.
Group: Documentation

%description doc
doc components for the SDL package.


%package lib
Summary: lib components for the SDL package.
Group: Libraries

%description lib
lib components for the SDL package.


%package lib32
Summary: lib32 components for the SDL package.
Group: Default

%description lib32
lib32 components for the SDL package.


%prep
%setup -q -n SDL-1.2.15
%patch1 -p1
pushd ..
cp -a SDL-1.2.15 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484496708
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1484496708
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sdl-config

%files dev
%defattr(-,root,root,-)
/usr/include/SDL/SDL.h
/usr/include/SDL/SDL_active.h
/usr/include/SDL/SDL_audio.h
/usr/include/SDL/SDL_byteorder.h
/usr/include/SDL/SDL_cdrom.h
/usr/include/SDL/SDL_config.h
/usr/include/SDL/SDL_cpuinfo.h
/usr/include/SDL/SDL_endian.h
/usr/include/SDL/SDL_error.h
/usr/include/SDL/SDL_events.h
/usr/include/SDL/SDL_getenv.h
/usr/include/SDL/SDL_joystick.h
/usr/include/SDL/SDL_keyboard.h
/usr/include/SDL/SDL_keysym.h
/usr/include/SDL/SDL_loadso.h
/usr/include/SDL/SDL_main.h
/usr/include/SDL/SDL_mouse.h
/usr/include/SDL/SDL_mutex.h
/usr/include/SDL/SDL_name.h
/usr/include/SDL/SDL_opengl.h
/usr/include/SDL/SDL_platform.h
/usr/include/SDL/SDL_quit.h
/usr/include/SDL/SDL_rwops.h
/usr/include/SDL/SDL_stdinc.h
/usr/include/SDL/SDL_syswm.h
/usr/include/SDL/SDL_thread.h
/usr/include/SDL/SDL_timer.h
/usr/include/SDL/SDL_types.h
/usr/include/SDL/SDL_version.h
/usr/include/SDL/SDL_video.h
/usr/include/SDL/begin_code.h
/usr/include/SDL/close_code.h
/usr/lib64/libSDL.so
/usr/lib64/pkgconfig/sdl.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libSDL.so
/usr/lib32/pkgconfig/32sdl.pc
/usr/lib32/pkgconfig/sdl.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL-1.2.so.0
/usr/lib64/libSDL-1.2.so.0.11.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libSDL-1.2.so.0
/usr/lib32/libSDL-1.2.so.0.11.4
