Name:          jackson-module-jaxb-annotations
Version:       2.2.2
Release:       4%{?dist}
Summary:       JAXB annotations support for Jackson (2.x)
License:       ASL 2.0
URL:           http://wiki.fasterxml.com/JacksonJAXBAnnotations
Source0:       https://github.com/FasterXML/jackson-module-jaxb-annotations/archive/%{name}-%{version}.tar.gz
# jackson-module-jaxb-annotations package don't include the license file
# https://github.com/FasterXML/jackson-module-jaxb-annotations/issues/21
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires: java-devel
BuildRequires: mvn(com.fasterxml:oss-parent)

# Require glassfish-jaxb-api
BuildRequires: mvn(javax.xml.bind:jaxb-api)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)

# test deps
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(junit:junit)

BuildRequires: maven-local
BuildRequires: maven-enforcer-plugin
BuildRequires: maven-plugin-build-helper
BuildRequires: maven-plugin-bundle
BuildRequires: maven-site-plugin
BuildRequires: maven-surefire-provider-junit4
BuildRequires: replacer
# bundle-plugin Requires
#BuildRequires: mvn(org.sonatype.aether:aether)

Provides:      jackson2-module-jaxb-annotations = %{version}-%{release}
Obsoletes:     jackson2-module-jaxb-annotations < %{version}-%{release}

BuildArch:     noarch

%description
Support for using JAXB annotations as an alternative to
"native" Jackson annotations, for configuring data binding.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} .
sed -i 's/\r//' LICENSE-2.0.txt

%build

%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.md

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.2-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 gil cattaneo <puntogil@libero.it> 2.2.2-2
- review fixes

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 2.2.2-1
- 2.2.2
- renamed jackson-module-jaxb-annotations

* Tue Jul 16 2013 gil cattaneo <puntogil@libero.it> 2.2.1-1
- 2.2.1

* Wed Oct 24 2012 gil cattaneo <puntogil@libero.it> 2.1.0-1
- update to 2.1.0
- renamed jackson2-module-jaxb-annotations

* Thu Sep 13 2012 gil cattaneo <puntogil@libero.it> 2.0.5-1
- initial rpm