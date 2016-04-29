#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SDL
Version  : 1.2.15
Release  : 4
URL      : https://www.libsdl.org/release/SDL-1.2.15.tar.gz
Source0  : https://www.libsdl.org/release/SDL-1.2.15.tar.gz
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0 LGPL-2.1
Requires: SDL-bin
Requires: SDL-lib
Requires: SDL-doc
BuildRequires : glibc-staticdev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(ice)
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


%prep
%setup -q -n SDL-1.2.15
%patch1 -p1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
