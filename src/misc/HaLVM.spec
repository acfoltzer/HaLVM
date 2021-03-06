%define debug_package %{nil}
Name:		HaLVM
Version:	2.0.0
Release:	2%{?dist}
Summary:	The Haskell Lightweight Virtual Machine

Group:		System Environment/Base
License:	BSD3
URL:		https://github.com/GaloisInc/HaLVM
Source0:	HaLVM.tar.gz

BuildRequires:	autoconf automake libtool patch gcc ncurses-devel
BuildRequires:  zlib-devel chrpath
BuildRequires:  /usr/include/xen/xen.h
Requires:       perl glibc libffi libgcc ncurses-libs zlib
Requires:       /usr/include/xen/xen.h
AutoReq:        no

%description
The Haskell Lightweight Virtual Machine, or HaLVM, is a port of the
Glasgow Haskell Compiler toolsuite to enable developers to write
high-level, lightweight virtual machines that can run directly on the
Xen hypervisor.

%prep
%setup -q -n HaLVM

%build
# We can't used %%configure because it overwrites halvm-ghc/config.sub for
# no apparant reasons
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix}  --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} --infodir=%{_infodir}
make 

%install
make install DESTDIR=%{buildroot}
chrpath -d %{buildroot}%{_libdir}/HaLVM-%{version}/bin/*
rm -rf  %{buildroot}share
mv %{buildroot}%{_docdir}/ghc %{buildroot}%{_docdir}/HaLVM-ghc
mv %{buildroot}%{_mandir}/man1/ghc.1 %{buildroot}%{_mandir}/man1/halvm-ghc.1
mkdir -p %{buildroot}%{_datadir}/HaLVM-%{version}
cp -r examples %{buildroot}%{_datadir}/HaLVM-%{version}/

%post
%{_bindir}/halvm-ghc-pkg recache

%files
%defattr(-,root,root)
%{_libdir}/HaLVM-%{version}/*
%{_libdir}/libIVC.a
%{_bindir}/convert-profile
%{_bindir}/halvm-cabal
%{_bindir}/halvm-config
%{_bindir}/halvm-ghc
%{_bindir}/halvm-ghc-pkg
%{_bindir}/mkrenddir
%{_bindir}/*-unknown-HaLVM-ghc*
%{_bindir}/*-unknown-HaLVM-hp2ps
%{_includedir}/libIVC.h
%{_docdir}/HaLVM-ghc/html/libraries/array-0.5.0.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/base-4.7.0.2/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/binary-0.7.1.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/bytestring-0.10.4.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/containers-0.5.5.1/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/deepseq-1.3.0.2/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/filepath-1.3.0.2/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/ghc-prim-0.3.1.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/haskell2010-1.1.2.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/hoopl-3.10.0.1/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/integer-simple-0.1.1.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/old-locale-1.0.0.6/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/old-time-1.1.0.2/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/pretty-1.1.1.1/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/template-haskell-2.9.0.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/time-1.4.2/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/transformers-0.3.0.0/LICENSE
%{_docdir}/HaLVM-ghc/html/libraries/xhtml-3000.2.1/LICENSE
%{_mandir}/man1/halvm-ghc.1.gz
%{_datadir}/HaLVM-%{version}/*

%changelog
* Thu Jul 02 2015 Adam Wick <awick@galois.com>
- Initial RPM release.
