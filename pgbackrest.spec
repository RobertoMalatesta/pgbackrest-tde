Summary:   pgBackRest 2.28-TDE
Name:      pgbackrest-tde
Version:   1.0.1
Release:   1
License:   MIT
BuildRoot: %{_topdir}/buildroot
AutoReq:   off
AutoProv:  off
Packager:  Patrick Thomschitz <patrick.thomschitz@cybertec.at>
BuildArch: x86_64
Prefix:    /usr/bin
Source:    pgbackrest-tde-1.0.1.tar.gz

# No Debug infos
%define debug_package %{nil}

%description
pgBAckRest 2.27-TDE

%prep
%setup -q

%build
cd src/
./configure
make

%install
cd src/
R=$RPM_BUILD_ROOT
rm -rf $R
mkdir -p $R
make install DESTDIR=$R

%files
%defattr(0755,postgres,postgres,0755)
/
#%changelog
#* Thu Jul 02 2020 Patrick Thomschitz
#- creation
