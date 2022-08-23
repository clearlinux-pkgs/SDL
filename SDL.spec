#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL
Version  : 1.2.15
Release  : 38
URL      : https://www.libsdl.org/release/SDL-1.2.15.tar.gz
Source0  : https://www.libsdl.org/release/SDL-1.2.15.tar.gz
Source1  : https://www.libsdl.org/release/SDL-1.2.15.tar.gz.sig
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: SDL-bin = %{version}-%{release}
Requires: SDL-lib = %{version}-%{release}
Requires: SDL-license = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : glibc-staticdev
BuildRequires : nasm-bin
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
Patch2: likely.patch
Patch3: CVE-2019-7574.patch
Patch4: CVE-2019-7577.patch
Patch5: CVE-2019-7572.patch
Patch6: CVE-2019-7578.patch
Patch7: CVE-2019-7575.patch
Patch8: CVE-2019-7638.patch
Patch9: CVE-2019-7636.nopatch
Patch10: CVE-2019-7635.patch
Patch11: CVE-2019-7637.patch
Patch12: CVE-2019-13616.patch
Patch13: SDL-1.2.15-no-default-backing-store.patch

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the SDL package.
Group: Binaries
Requires: SDL-license = %{version}-%{release}

%description bin
bin components for the SDL package.


%package dev
Summary: dev components for the SDL package.
Group: Development
Requires: SDL-lib = %{version}-%{release}
Requires: SDL-bin = %{version}-%{release}
Provides: SDL-devel = %{version}-%{release}
Requires: SDL = %{version}-%{release}

%description dev
dev components for the SDL package.


%package lib
Summary: lib components for the SDL package.
Group: Libraries
Requires: SDL-license = %{version}-%{release}

%description lib
lib components for the SDL package.


%package license
Summary: license components for the SDL package.
Group: Default

%description license
license components for the SDL package.


%prep
%setup -q -n SDL-1.2.15
cd %{_builddir}/SDL-1.2.15
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
pushd ..
cp -a SDL-1.2.15 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656362206
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
%configure --disable-static --disable-rpath
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --disable-rpath
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1656362206
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL
cp %{_builddir}/SDL-1.2.15/COPYING %{buildroot}/usr/share/package-licenses/SDL/720ac006232639ed551ce48d638dee35f8d378d4
cp %{_builddir}/SDL-1.2.15/Xcode/SDL/pkg-support/resources/License.rtf %{buildroot}/usr/share/package-licenses/SDL/a6e94b0f7b8b11f4d640936574684dbe70c10a49
cp %{_builddir}/SDL-1.2.15/src/hermes/COPYING.LIB %{buildroot}/usr/share/package-licenses/SDL/293ea6c85b498c82ead8a6fb17ea22df24d8f798
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/glibc-hwcaps/x86-64-v3/libSDL.so
/usr/lib64/libSDL.so
/usr/lib64/pkgconfig/sdl.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/SDLKey.3
/usr/share/man/man3/SDL_ActiveEvent.3
/usr/share/man/man3/SDL_AddTimer.3
/usr/share/man/man3/SDL_AudioCVT.3
/usr/share/man/man3/SDL_AudioSpec.3
/usr/share/man/man3/SDL_BlitSurface.3
/usr/share/man/man3/SDL_BuildAudioCVT.3
/usr/share/man/man3/SDL_CD.3
/usr/share/man/man3/SDL_CDClose.3
/usr/share/man/man3/SDL_CDEject.3
/usr/share/man/man3/SDL_CDName.3
/usr/share/man/man3/SDL_CDNumDrives.3
/usr/share/man/man3/SDL_CDOpen.3
/usr/share/man/man3/SDL_CDPause.3
/usr/share/man/man3/SDL_CDPlay.3
/usr/share/man/man3/SDL_CDPlayTracks.3
/usr/share/man/man3/SDL_CDResume.3
/usr/share/man/man3/SDL_CDStatus.3
/usr/share/man/man3/SDL_CDStop.3
/usr/share/man/man3/SDL_CDtrack.3
/usr/share/man/man3/SDL_CloseAudio.3
/usr/share/man/man3/SDL_Color.3
/usr/share/man/man3/SDL_CondBroadcast.3
/usr/share/man/man3/SDL_CondSignal.3
/usr/share/man/man3/SDL_CondWait.3
/usr/share/man/man3/SDL_CondWaitTimeout.3
/usr/share/man/man3/SDL_ConvertAudio.3
/usr/share/man/man3/SDL_ConvertSurface.3
/usr/share/man/man3/SDL_CreateCond.3
/usr/share/man/man3/SDL_CreateCursor.3
/usr/share/man/man3/SDL_CreateMutex.3
/usr/share/man/man3/SDL_CreateRGBSurface.3
/usr/share/man/man3/SDL_CreateRGBSurfaceFrom.3
/usr/share/man/man3/SDL_CreateSemaphore.3
/usr/share/man/man3/SDL_CreateThread.3
/usr/share/man/man3/SDL_CreateYUVOverlay.3
/usr/share/man/man3/SDL_Delay.3
/usr/share/man/man3/SDL_DestroyCond.3
/usr/share/man/man3/SDL_DestroyMutex.3
/usr/share/man/man3/SDL_DestroySemaphore.3
/usr/share/man/man3/SDL_DisplayFormat.3
/usr/share/man/man3/SDL_DisplayFormatAlpha.3
/usr/share/man/man3/SDL_DisplayYUVOverlay.3
/usr/share/man/man3/SDL_EnableKeyRepeat.3
/usr/share/man/man3/SDL_EnableUNICODE.3
/usr/share/man/man3/SDL_Event.3
/usr/share/man/man3/SDL_EventState.3
/usr/share/man/man3/SDL_ExposeEvent.3
/usr/share/man/man3/SDL_FillRect.3
/usr/share/man/man3/SDL_Flip.3
/usr/share/man/man3/SDL_FreeCursor.3
/usr/share/man/man3/SDL_FreeSurface.3
/usr/share/man/man3/SDL_FreeWAV.3
/usr/share/man/man3/SDL_FreeYUVOverlay.3
/usr/share/man/man3/SDL_GL_GetAttribute.3
/usr/share/man/man3/SDL_GL_GetProcAddress.3
/usr/share/man/man3/SDL_GL_LoadLibrary.3
/usr/share/man/man3/SDL_GL_SetAttribute.3
/usr/share/man/man3/SDL_GL_SwapBuffers.3
/usr/share/man/man3/SDL_GLattr.3
/usr/share/man/man3/SDL_GetAppState.3
/usr/share/man/man3/SDL_GetAudioStatus.3
/usr/share/man/man3/SDL_GetClipRect.3
/usr/share/man/man3/SDL_GetCursor.3
/usr/share/man/man3/SDL_GetError.3
/usr/share/man/man3/SDL_GetEventFilter.3
/usr/share/man/man3/SDL_GetGamma.3
/usr/share/man/man3/SDL_GetGammaRamp.3
/usr/share/man/man3/SDL_GetKeyName.3
/usr/share/man/man3/SDL_GetKeyState.3
/usr/share/man/man3/SDL_GetModState.3
/usr/share/man/man3/SDL_GetMouseState.3
/usr/share/man/man3/SDL_GetRGB.3
/usr/share/man/man3/SDL_GetRGBA.3
/usr/share/man/man3/SDL_GetRelativeMouseState.3
/usr/share/man/man3/SDL_GetThreadID.3
/usr/share/man/man3/SDL_GetTicks.3
/usr/share/man/man3/SDL_GetVideoInfo.3
/usr/share/man/man3/SDL_GetVideoSurface.3
/usr/share/man/man3/SDL_Init.3
/usr/share/man/man3/SDL_InitSubSystem.3
/usr/share/man/man3/SDL_JoyAxisEvent.3
/usr/share/man/man3/SDL_JoyBallEvent.3
/usr/share/man/man3/SDL_JoyButtonEvent.3
/usr/share/man/man3/SDL_JoyHatEvent.3
/usr/share/man/man3/SDL_JoystickClose.3
/usr/share/man/man3/SDL_JoystickEventState.3
/usr/share/man/man3/SDL_JoystickGetAxis.3
/usr/share/man/man3/SDL_JoystickGetBall.3
/usr/share/man/man3/SDL_JoystickGetButton.3
/usr/share/man/man3/SDL_JoystickGetHat.3
/usr/share/man/man3/SDL_JoystickIndex.3
/usr/share/man/man3/SDL_JoystickName.3
/usr/share/man/man3/SDL_JoystickNumAxes.3
/usr/share/man/man3/SDL_JoystickNumBalls.3
/usr/share/man/man3/SDL_JoystickNumButtons.3
/usr/share/man/man3/SDL_JoystickNumHats.3
/usr/share/man/man3/SDL_JoystickOpen.3
/usr/share/man/man3/SDL_JoystickOpened.3
/usr/share/man/man3/SDL_JoystickUpdate.3
/usr/share/man/man3/SDL_KeyboardEvent.3
/usr/share/man/man3/SDL_KillThread.3
/usr/share/man/man3/SDL_ListModes.3
/usr/share/man/man3/SDL_LoadBMP.3
/usr/share/man/man3/SDL_LoadWAV.3
/usr/share/man/man3/SDL_LockAudio.3
/usr/share/man/man3/SDL_LockSurface.3
/usr/share/man/man3/SDL_LockYUVOverlay.3
/usr/share/man/man3/SDL_MapRGB.3
/usr/share/man/man3/SDL_MapRGBA.3
/usr/share/man/man3/SDL_MixAudio.3
/usr/share/man/man3/SDL_MouseButtonEvent.3
/usr/share/man/man3/SDL_MouseMotionEvent.3
/usr/share/man/man3/SDL_NumJoysticks.3
/usr/share/man/man3/SDL_OpenAudio.3
/usr/share/man/man3/SDL_Overlay.3
/usr/share/man/man3/SDL_Palette.3
/usr/share/man/man3/SDL_PauseAudio.3
/usr/share/man/man3/SDL_PeepEvents.3
/usr/share/man/man3/SDL_PixelFormat.3
/usr/share/man/man3/SDL_PollEvent.3
/usr/share/man/man3/SDL_PumpEvents.3
/usr/share/man/man3/SDL_PushEvent.3
/usr/share/man/man3/SDL_Quit.3
/usr/share/man/man3/SDL_QuitEvent.3
/usr/share/man/man3/SDL_QuitSubSystem.3
/usr/share/man/man3/SDL_RWFromFile.3
/usr/share/man/man3/SDL_Rect.3
/usr/share/man/man3/SDL_RemoveTimer.3
/usr/share/man/man3/SDL_ResizeEvent.3
/usr/share/man/man3/SDL_SaveBMP.3
/usr/share/man/man3/SDL_SemPost.3
/usr/share/man/man3/SDL_SemTryWait.3
/usr/share/man/man3/SDL_SemValue.3
/usr/share/man/man3/SDL_SemWait.3
/usr/share/man/man3/SDL_SemWaitTimeout.3
/usr/share/man/man3/SDL_SetAlpha.3
/usr/share/man/man3/SDL_SetClipRect.3
/usr/share/man/man3/SDL_SetColorKey.3
/usr/share/man/man3/SDL_SetColors.3
/usr/share/man/man3/SDL_SetCursor.3
/usr/share/man/man3/SDL_SetEventFilter.3
/usr/share/man/man3/SDL_SetGamma.3
/usr/share/man/man3/SDL_SetGammaRamp.3
/usr/share/man/man3/SDL_SetModState.3
/usr/share/man/man3/SDL_SetPalette.3
/usr/share/man/man3/SDL_SetTimer.3
/usr/share/man/man3/SDL_SetVideoMode.3
/usr/share/man/man3/SDL_ShowCursor.3
/usr/share/man/man3/SDL_Surface.3
/usr/share/man/man3/SDL_SysWMEvent.3
/usr/share/man/man3/SDL_ThreadID.3
/usr/share/man/man3/SDL_UnlockAudio.3
/usr/share/man/man3/SDL_UnlockSurface.3
/usr/share/man/man3/SDL_UnlockYUVOverlay.3
/usr/share/man/man3/SDL_UpdateRect.3
/usr/share/man/man3/SDL_UpdateRects.3
/usr/share/man/man3/SDL_UserEvent.3
/usr/share/man/man3/SDL_VideoDriverName.3
/usr/share/man/man3/SDL_VideoInfo.3
/usr/share/man/man3/SDL_VideoModeOK.3
/usr/share/man/man3/SDL_WM_GetCaption.3
/usr/share/man/man3/SDL_WM_GrabInput.3
/usr/share/man/man3/SDL_WM_IconifyWindow.3
/usr/share/man/man3/SDL_WM_SetCaption.3
/usr/share/man/man3/SDL_WM_SetIcon.3
/usr/share/man/man3/SDL_WM_ToggleFullScreen.3
/usr/share/man/man3/SDL_WaitEvent.3
/usr/share/man/man3/SDL_WaitThread.3
/usr/share/man/man3/SDL_WarpMouse.3
/usr/share/man/man3/SDL_WasInit.3
/usr/share/man/man3/SDL_keysym.3
/usr/share/man/man3/SDL_mutexP.3
/usr/share/man/man3/SDL_mutexV.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libSDL-1.2.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libSDL-1.2.so.0.11.4
/usr/lib64/libSDL-1.2.so.0
/usr/lib64/libSDL-1.2.so.0.11.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL/293ea6c85b498c82ead8a6fb17ea22df24d8f798
/usr/share/package-licenses/SDL/720ac006232639ed551ce48d638dee35f8d378d4
/usr/share/package-licenses/SDL/a6e94b0f7b8b11f4d640936574684dbe70c10a49
