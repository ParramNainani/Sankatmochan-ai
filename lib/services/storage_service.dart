import 'dart:io';
import 'dart:typed_data';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:path/path.dart' as path;

class StorageService {
  final FirebaseStorage _storage = FirebaseStorage.instance;
  final FirebaseFirestore _firestore = FirebaseFirestore.instance;

  /// Upload chart image to Firebase Storage and save metadata to Firestore
  Future<String> uploadChartImage({
    required String personName,
    required DateTime birthDate,
    required String birthTime,
    required String birthPlace,
    required File chartImageFile,
  }) async {
    try {
      // Create unique filename
      final timestamp = DateTime.now().millisecondsSinceEpoch;
      final fileName =
          'charts/${personName.replaceAll(' ', '_')}_${timestamp}.png';

      // Upload image to Firebase Storage
      final storageRef = _storage.ref().child(fileName);
      final uploadTask = storageRef.putFile(chartImageFile);
      final snapshot = await uploadTask;
      final downloadUrl = await snapshot.ref.getDownloadURL();

      // Save metadata to Firestore
      await _firestore.collection('birth_charts').add({
        'person_name': personName,
        'birth_date': birthDate.toIso8601String(),
        'birth_time': birthTime,
        'birth_place': birthPlace,
        'chart_image_url': downloadUrl,
        'chart_image_path': fileName,
        'created_at': FieldValue.serverTimestamp(),
        'updated_at': FieldValue.serverTimestamp(),
      });

      return downloadUrl;
    } catch (e) {
      throw Exception('Failed to upload chart image: $e');
    }
  }

  /// Upload chart image from bytes (for backend integration)
  Future<String> uploadChartImageFromBytes({
    required String personName,
    required DateTime birthDate,
    required String birthTime,
    required String birthPlace,
    required Uint8List imageBytes,
  }) async {
    try {
      // Create unique filename
      final timestamp = DateTime.now().millisecondsSinceEpoch;
      final fileName =
          'charts/${personName.replaceAll(' ', '_')}_${timestamp}.png';

      // Upload image to Firebase Storage
      final storageRef = _storage.ref().child(fileName);
      final uploadTask = storageRef.putData(imageBytes);
      final snapshot = await uploadTask;
      final downloadUrl = await snapshot.ref.getDownloadURL();

      // Save metadata to Firestore
      await _firestore.collection('birth_charts').add({
        'person_name': personName,
        'birth_date': birthDate.toIso8601String(),
        'birth_time': birthTime,
        'birth_place': birthPlace,
        'chart_image_url': downloadUrl,
        'chart_image_path': fileName,
        'created_at': FieldValue.serverTimestamp(),
        'updated_at': FieldValue.serverTimestamp(),
      });

      return downloadUrl;
    } catch (e) {
      throw Exception('Failed to upload chart image: $e');
    }
  }

  /// Get all birth charts from Firestore
  Future<List<Map<String, dynamic>>> getAllBirthCharts() async {
    try {
      final querySnapshot = await _firestore
          .collection('birth_charts')
          .orderBy('created_at', descending: true)
          .get();

      return querySnapshot.docs.map((doc) {
        final data = doc.data();
        data['id'] = doc.id;
        return data;
      }).toList();
    } catch (e) {
      throw Exception('Failed to fetch birth charts: $e');
    }
  }

  /// Get birth chart by ID
  Future<Map<String, dynamic>?> getBirthChartById(String chartId) async {
    try {
      final doc =
          await _firestore.collection('birth_charts').doc(chartId).get();
      if (doc.exists) {
        final data = doc.data()!;
        data['id'] = doc.id;
        return data;
      }
      return null;
    } catch (e) {
      throw Exception('Failed to fetch birth chart: $e');
    }
  }

  /// Delete birth chart and its image
  Future<void> deleteBirthChart(String chartId) async {
    try {
      // Get chart data first
      final chartData = await getBirthChartById(chartId);
      if (chartData != null) {
        // Delete image from Storage
        final imagePath = chartData['chart_image_path'];
        if (imagePath != null) {
          await _storage.ref().child(imagePath).delete();
        }

        // Delete document from Firestore
        await _firestore.collection('birth_charts').doc(chartId).delete();
      }
    } catch (e) {
      throw Exception('Failed to delete birth chart: $e');
    }
  }

  /// Search birth charts by person name
  Future<List<Map<String, dynamic>>> searchBirthChartsByName(
      String name) async {
    try {
      final querySnapshot = await _firestore
          .collection('birth_charts')
          .where('person_name', isGreaterThanOrEqualTo: name)
          .where('person_name', isLessThan: name + '\uf8ff')
          .orderBy('person_name')
          .get();

      return querySnapshot.docs.map((doc) {
        final data = doc.data();
        data['id'] = doc.id;
        return data;
      }).toList();
    } catch (e) {
      throw Exception('Failed to search birth charts: $e');
    }
  }
}
