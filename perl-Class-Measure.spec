#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Measure
Version  : 0.08
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/Class-Measure-0.08.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BL/BLUEFEET/Class-Measure-0.08.tar.gz
Summary  : 'Create, compare, and convert units of measurement.'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Measure-license = %{version}-%{release}
Requires: perl-Class-Measure-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
# NAME
Class::Measure - Create, compare, and convert units of measurement.
# SYNOPSIS

%package dev
Summary: dev components for the perl-Class-Measure package.
Group: Development
Provides: perl-Class-Measure-devel = %{version}-%{release}
Requires: perl-Class-Measure = %{version}-%{release}

%description dev
dev components for the perl-Class-Measure package.


%package license
Summary: license components for the perl-Class-Measure package.
Group: Default

%description license
license components for the perl-Class-Measure package.


%package perl
Summary: perl components for the perl-Class-Measure package.
Group: Default
Requires: perl-Class-Measure = %{version}-%{release}

%description perl
perl components for the perl-Class-Measure package.


%prep
%setup -q -n Class-Measure-0.08
cd %{_builddir}/Class-Measure-0.08

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Measure
cp %{_builddir}/Class-Measure-0.08/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Measure/224f103b390d1c8dbaaf3d9660fea6bad84bbaa5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Measure.3
/usr/share/man/man3/Class::Measure::Length.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Measure/224f103b390d1c8dbaaf3d9660fea6bad84bbaa5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Class/Measure.pm
/usr/lib/perl5/vendor_perl/5.30.3/Class/Measure/Length.pm
