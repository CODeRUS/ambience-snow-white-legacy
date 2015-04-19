Name:       ambience-show-white-legacy

Summary:    Sailfish Jolla ambience
Version:    0.0.2
Release:    10.2.1.jolla
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch
Requires:   ambienced
Summary:    Try out how The Other Half changes the mood of your Jolla.

%description
The Other Half - Snow White with an especially designed Ambience -  created to match The Other Half perfectly. Legacy version.

%prep
%setup -q

# >> setup
# << setup

%build
# >> build pre
# << build pre

# >> build post
# << build post

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{_datadir}/ambience/ambience-snow-white-legacy
install -m 644 ambience-snow-white-legacy.ambience %{buildroot}%{_datadir}/ambience/ambience-snow-white-legacy
mkdir -p  %{buildroot}%{_datadir}/ambience/ambience-snow-white-legacy/images/
install -m 644 images/Snow_White_Legacy.jpg %{buildroot}%{_datadir}/ambience/ambience-snow-white-legacy/images/
mkdir -p  %{buildroot}%{_datadir}/translations/
install -m 644 translations/ambience-snow-white-legacy_eng_en.qm %{buildroot}%{_datadir}/translations/
# >> install pre
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_datadir}/ambience/ambience-snow-white-legacy/ambience-snow-white-legacy.ambience
%{_datadir}/ambience/ambience-snow-white-legacy/images/Snow_White_Legacy.jpg
%{_datadir}/translations/ambience-snow-white-legacy_eng_en.qm 

%clean
rm -rf %{buildroot}